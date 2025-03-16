import logging

import heapq
import torch
import numpy as np
from contextlib import nullcontext
from tqdm import trange

from .Evaluator import Evaluator
from .utils import cos_sim

from sentence_transformers.similarity_functions import SimilarityFunction

logger = logging.getLogger(__name__)


class InstructionRetrievalEvaluator(Evaluator):
    """
    This class evaluates an Information Retrieval (IR) setting.

    Given a set of queries and a large corpus set. It will retrieve for each query the top-k most similar document. It measures
    Mean Reciprocal Rank (MRR), Recall@k, and Normalized Discounted Cumulative Gain (NDCG)
    

    :param queries: A dictionary mapping query IDs to queries.
    :param corpus: A dictionary mapping document IDs to documents.
    :param relevant_docs: A dictionary mapping query IDs to a set of relevant document IDs.
    :param corpus_chunk_size: The size of each chunk of the corpus. Defaults to 50.
    :param mrr_at_k: A list of integers representing the values of k for MRR calculation. Defaults to [10].
    :param ndcg_at_k: A list of integers representing the values of k for NDCG calculation. Defaults to [5].
    :param accuracy_at_k: A list of integers representing the values of k for accuracy calculation. Defaults to [1, 3, 5, 10].
    :param precision_recall_at_k: A list of integers representing the values of k for precision and recall calculation. Defaults to [1, 3, 5, 10].
    :param map_at_k: A list of integers representing the values of k for MAP calculation. Defaults to [100].
    :param show_progress_bar: Whether to show a progress bar during evaluation. Defaults to False.
    :param batch_size: The batch size for evaluation. Defaults to 32.
    :param name: A name for the evaluation. Defaults to "".
    :param write_csv: Whether to write the evaluation results to a CSV file. Defaults to True.
    :param truncate_dim: The dimension to truncate the embeddings to. Defaults to None.
    :param score_functions: A dictionary mapping score function names to score functions. Defaults to the ``similarity`` function from the ``model``.
    :param main_score_function: The main score function to use for evaluation. Defaults to None.
    :param query_prompt: The prompt to be used when encoding the corpus. Defaults to None.
    :param query_prompt_name: The name of the prompt to be used when encoding the corpus. Defaults to None.
    :param corpus_prompt: The prompt to be used when encoding the corpus. Defaults to None.
    :param corpus_prompt_name: The name of the prompt to be used when encoding the corpus. Defaults to None.
    """

    def __init__(
        self,
        queries,
        corpus,
        relevant_docs,
        corpus_chunk_size=50,
        mrr_at_k=[10],
        ndcg_at_k=[5],
        accuracy_at_k=[1, 3, 5, 10],
        precision_recall_at_k=[1, 3, 5, 10],
        map_at_k=[100],
        show_progress_bar=False,
        batch_size=32,
        name="",
        write_csv=True,
        truncate_dim=None,
        score_functions=None,
        main_score_function=None,
        query_prompt=None,
        query_prompt_name=None,
        corpus_prompt=None,
        corpus_prompt_name=None,
    ):
        super().__init__()
        self.queries_ids = []
        for qid in queries:
            if qid in relevant_docs and len(relevant_docs[qid]) > 0:
                self.queries_ids.append(qid)

        self.queries = [queries[qid] for qid in self.queries_ids]

        self.corpus_ids = list(corpus.keys())
        self.corpus = [corpus[cid] for cid in self.corpus_ids]

        self.query_prompt = query_prompt
        self.query_prompt_name = query_prompt_name
        self.corpus_prompt = corpus_prompt
        self.corpus_prompt_name = corpus_prompt_name

        self.relevant_docs = relevant_docs
        self.corpus_chunk_size = corpus_chunk_size
        self.mrr_at_k = mrr_at_k
        self.ndcg_at_k = ndcg_at_k
        self.accuracy_at_k = accuracy_at_k
        self.precision_recall_at_k = precision_recall_at_k
        self.map_at_k = map_at_k

        self.show_progress_bar = show_progress_bar
        self.batch_size = batch_size
        self.name = name
        self.write_csv = write_csv
        self.score_functions = score_functions
        self.score_function_names = sorted(list(self.score_functions.keys())) if score_functions else []
        self.main_score_function = SimilarityFunction(main_score_function) if main_score_function else None
        self.truncate_dim = truncate_dim

        if name:
            name = "_" + name


    def __call__(self, model):
        scores = self.compute_metrices(model)
    
        return scores

    def compute_metrices(self, model, corpus_model=None, corpus_embeddings=None):
        if self.score_functions is None:
            self.score_functions = {'cos_sim': cos_sim}
            self.score_function_names = ['cos_sim']

        if corpus_model is None:
            corpus_model = model

        max_k = max(
            max(self.mrr_at_k),
            max(self.ndcg_at_k),
            max(self.accuracy_at_k),
            max(self.precision_recall_at_k),
            max(self.map_at_k),
        )

        logger.info(f"Encoding {len(self.queries)} queries...")
        # Compute embedding for the queries
        with nullcontext() if self.truncate_dim is None else model.truncate_sentence_embeddings(self.truncate_dim):
            query_embeddings = model.encode(
                self.queries,
                prompt_name=self.query_prompt_name,
                prompt=self.query_prompt,
                batch_size=self.batch_size,
                show_progress_bar=self.show_progress_bar,
                convert_to_tensor=True,
            )

        queries_result_list = {}
        for name in self.score_functions:
            queries_result_list[name] = [[] for _ in range(len(query_embeddings))]

        logger.info(f"Encoding {len(self.corpus)} corpus...")
        # Iterate over chunks of the corpus
        for corpus_start_idx in trange(
            0, len(self.corpus), self.corpus_chunk_size, desc="Corpus Chunks", disable=not self.show_progress_bar
        ):
            corpus_end_idx = min(corpus_start_idx + self.corpus_chunk_size, len(self.corpus))

            # Encode chunk of corpus
            if corpus_embeddings is None:
                with (
                    nullcontext()
                    if self.truncate_dim is None
                    else corpus_model.truncate_sentence_embeddings(self.truncate_dim)
                ):
                    sub_corpus_embeddings = corpus_model.encode(
                        self.corpus[corpus_start_idx:corpus_end_idx],
                        prompt_name=self.corpus_prompt_name,
                        prompt=self.corpus_prompt,
                        batch_size=self.batch_size,
                        show_progress_bar=False,
                        convert_to_tensor=True,
                    )
            else:
                sub_corpus_embeddings = corpus_embeddings[corpus_start_idx:corpus_end_idx]

            # Compute cosine similarites
            for name, score_function in self.score_functions.items():
                pair_scores = score_function(query_embeddings, sub_corpus_embeddings)

                # Get top-k values
                pair_scores_top_k_values, pair_scores_top_k_idx = torch.topk(
                    pair_scores, min(max_k, len(pair_scores[0])), dim=1, largest=True, sorted=False
                )
                pair_scores_top_k_values = pair_scores_top_k_values.cpu().tolist()
                pair_scores_top_k_idx = pair_scores_top_k_idx.cpu().tolist()

                for query_itr in range(len(query_embeddings)):
                    for sub_corpus_id, score in zip(
                        pair_scores_top_k_idx[query_itr], pair_scores_top_k_values[query_itr]
                    ):
                        corpus_id = self.corpus_ids[corpus_start_idx + sub_corpus_id]
                        # NOTE: TREC/BEIR/MTEB skips cases where the corpus_id is the same as the query_id, e.g.:
                        # if corpus_id == self.queries_ids[query_itr]:
                        #     continue
                        # This is not done here, as this might be unexpected behaviour if the user just uses
                        # sets of integers from 0 as query_ids and corpus_ids.
                        if len(queries_result_list[name][query_itr]) < max_k:
                            # heaqp tracks the quantity of the first element in the tuple
                            heapq.heappush(queries_result_list[name][query_itr], (score, corpus_id))
                        else:
                            heapq.heappushpop(queries_result_list[name][query_itr], (score, corpus_id))

        for name in queries_result_list:
            for query_itr in range(len(queries_result_list[name])):
                for doc_itr in range(len(queries_result_list[name][query_itr])):
                    score, corpus_id = queries_result_list[name][query_itr][doc_itr]
                    queries_result_list[name][query_itr][doc_itr] = {"corpus_id": corpus_id, "score": score} 

        # Compute scores
        scores = {name: self.compute_metrics(queries_result_list[name]) for name in self.score_functions}
        final_scores = [self.output_scores(scores[name]) for name in self.score_functions]
        
        return final_scores[0]

    def compute_metrics(self, queries_result_list):
        # Init score computation values
        num_hits_at_k = {k: 0 for k in self.accuracy_at_k}
        precisions_at_k = {k: [] for k in self.precision_recall_at_k}
        recall_at_k = {k: [] for k in self.precision_recall_at_k}
        MRR = {k: 0 for k in self.mrr_at_k}
        ndcg = {k: [] for k in self.ndcg_at_k}
        AveP_at_k = {k: [] for k in self.map_at_k}

        # Compute scores on results
        for query_itr in range(len(queries_result_list)):
            query_id = self.queries_ids[query_itr]

            # Sort scores
            top_hits = sorted(queries_result_list[query_itr], key=lambda x: x["score"], reverse=True)
            query_relevant_docs = self.relevant_docs[query_id]

            # Accuracy@k - We count the result correct, if at least one relevant doc is across the top-k documents
            for k_val in self.accuracy_at_k:
                for hit in top_hits[0:k_val]:
                    if hit["corpus_id"] in query_relevant_docs:
                        num_hits_at_k[k_val] += 1
                        break

            # Precision and Recall@k
            for k_val in self.precision_recall_at_k:
                num_correct = 0
                for hit in top_hits[0:k_val]:
                    if hit["corpus_id"] in query_relevant_docs:
                        num_correct += 1

                precisions_at_k[k_val].append(num_correct / k_val)
                recall_at_k[k_val].append(num_correct / len(query_relevant_docs))

            # MRR@k
            for k_val in self.mrr_at_k:
                for rank, hit in enumerate(top_hits[0:k_val]):
                    if hit["corpus_id"] in query_relevant_docs:
                        MRR[k_val] += 1.0 / (rank + 1)
                        break

            # NDCG@k
            for k_val in self.ndcg_at_k:
                predicted_relevance = [
                    1 if top_hit["corpus_id"] in query_relevant_docs else 0 for top_hit in top_hits[0:k_val]
                ]
                true_relevances = [1] * len(query_relevant_docs)

                ndcg_value = self.compute_dcg_at_k(predicted_relevance, k_val) / self.compute_dcg_at_k(
                    true_relevances, k_val
                )
                ndcg[k_val].append(ndcg_value)

            # MAP@k
            for k_val in self.map_at_k:
                num_correct = 0
                sum_precisions = 0

                for rank, hit in enumerate(top_hits[0:k_val]):
                    if hit["corpus_id"] in query_relevant_docs:
                        num_correct += 1
                        sum_precisions += num_correct / (rank + 1)

                avg_precision = sum_precisions / min(k_val, len(query_relevant_docs))
                AveP_at_k[k_val].append(avg_precision)

        # Compute averages
        for k in num_hits_at_k:
            num_hits_at_k[k] /= len(self.queries)

        for k in precisions_at_k:
            precisions_at_k[k] = np.mean(precisions_at_k[k])

        for k in recall_at_k:
            recall_at_k[k] = np.mean(recall_at_k[k])

        for k in ndcg:
            ndcg[k] = np.mean(ndcg[k])

        for k in MRR:
            MRR[k] /= len(self.queries)

        for k in AveP_at_k:
            AveP_at_k[k] = np.mean(AveP_at_k[k])

        return {
            "accuracy@k": num_hits_at_k,
            "precision@k": precisions_at_k,
            "recall@k": recall_at_k,
            "ndcg@k": ndcg,
            "mrr@k": MRR,
            "map@k": AveP_at_k,
        }

    def output_scores(self, scores):
        final_scores = {}
        for k in scores["accuracy@k"]:
            score = {f"Accuracy@{k}": scores["accuracy@k"][k]}
            final_scores.update(score)

        for k in scores["precision@k"]:
            score = {f"precision@{k}": scores["precision@k"][k]}
            final_scores.update(score)

        for k in scores["recall@k"]:
            score = {f"recall@{k}": scores["recall@k"][k]}
            final_scores.update(score)

        for k in scores["mrr@k"]:
            score = {f"MRR@{k}": scores["mrr@k"][k]}
            final_scores.update(score)

        for k in scores["ndcg@k"]:
            score = {f"NDCG@{k}": scores["ndcg@k"][k]}
            final_scores.update(score)

        for k in scores["map@k"]:
            score = {f"MAP@{k}": scores["map@k"][k]}
            final_scores.update(score)

        return final_scores

    @staticmethod
    def compute_dcg_at_k(relevances, k):
        dcg = 0
        for i in range(min(len(relevances), k)):
            dcg += relevances[i] / np.log2(i + 2)  # +2 as we start our idx at 0
        return dcg