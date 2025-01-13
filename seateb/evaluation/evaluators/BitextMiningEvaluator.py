# import logging

# from contextlib import nullcontext
# import numpy as np
# import torch
# from sentence_transformers.util import pytorch_cos_sim

# from .Evaluator import Evaluator

# logger = logging.getLogger(__name__)


# class BitextMiningEvaluator(Evaluator):
#     """
#     Evaluate a model based on the similarity of the embeddings by calculating the accuracy of identifying similar and
#     dissimilar sentences.
#     The metrics are the cosine similarity
#     The returned score is the accuracy with a specified metric.
#     :param sentences1: The source language column of sentences
#     :param sentences2: The target language column of sentences
#     :param name: Name for the output
#     :param batch_size: Batch size used to compute embeddings
#     :param truncate_dim: The dimension to truncate sentence embeddings to. If None, the model's
#         current truncation dimension will be used. Defaults to None.
#     :param print_wrong_matches: Whether to print incorrect matches. Defaults to False.
#     :param write_csv: Write results to a CSV file
#     """

#     def __init__(
#         self, sentences1, sentences2, batch_size=4, limit=None, print_wrong_matches=False, truncate_dim=None, **kwargs
#     ):
#         super().__init__(**kwargs)
#         if limit:
#             sentences1 = sentences1[:limit]
#             sentences2 = sentences2[:limit]
#         self.sentences1 = sentences1
#         self.sentences2 = sentences2
#         self.batch_size = batch_size
#         self.truncate_dim = truncate_dim
#         self.print_wrong_matches = print_wrong_matches
        
#         assert len(self.sentences1) == len(self.sentences2)


#     def __call__(self, model):
#         scores = self.compute_metrics(model)
        
#         # Main score is the max of Average Precision (AP)
#         main_score = max(scores[short_name]["mean_accuracy"] for short_name in scores)
#         scores["main_score"] = main_score
#         return scores

#     def compute_metrics(self, model):

#         with nullcontext() if self.truncate_dim is None else model.truncate_sentence_embeddings(self.truncate_dim):
#             sentences = list(set(self.sentences1 + self.sentences2))
#             logger.info(f"Encoding {len(sentences)} sentences...")
#             embeddings = model.encode(sentences, batch_size=self.batch_size, convert_to_numpy=False)
#             emb_dict = {sent: emb for sent, emb in zip(sentences, embeddings)}
#             embeddings1 = torch.stack([emb_dict[sent] for sent in self.sentences1])
#             embeddings2 = torch.stack([emb_dict[sent] for sent in self.sentences2])
        
#         cos_sims = pytorch_cos_sim(embeddings1, embeddings2).detach().cpu().numpy()
        
#         correct_src2trg = 0
#         correct_trg2src = 0

#         for i in range(len(cos_sims)):
#             max_idx = np.argmax(cos_sims[i])

#             if i == max_idx:
#                 correct_src2trg += 1
#             elif self.print_wrong_matches:
#                 print("\nIncorrect  : Source", i, "is most similar to target", max_idx, "instead of target", i)
#                 print("Source     :", self.sentences1[i])
#                 print("Pred Target:", self.sentences2[max_idx], f"(Score: {cos_sims[i][max_idx]:.4f})")
#                 print("True Target:", self.sentences2[i], f"(Score: {cos_sims[i][i]:.4f})")

#                 results = enumerate(cos_sims[i])
#                 results = sorted(results, key=lambda x: x[1], reverse=True)
#                 for idx, score in results[:5]:
#                     print("\t", idx, f"(Score: {score:.4f})", self.sentences2[idx])

#         cos_sims = cos_sims.T
#         for i in range(len(cos_sims)):
#             max_idx = np.argmax(cos_sims[i])
#             if i == max_idx:
#                 correct_trg2src += 1

#         acc_src2trg = correct_src2trg / len(cos_sims)
#         acc_trg2src = correct_trg2src / len(cos_sims)

#         metrics = {
#             "src2trg_accuracy": acc_src2trg,
#             "trg2src_accuracy": acc_trg2src,
#             "mean_accuracy": (acc_src2trg + acc_trg2src) / 2,
#         }
        
#         return metrics


import logging

import numpy as np
import torch
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

from .Evaluator import Evaluator
from .utils import cos_sim


logger = logging.getLogger(__name__)


class BitextMiningEvaluator(Evaluator):
    def __init__(self, sentences1, sentences2, gold, batch_size=32, limit=None, **kwargs):
        super().__init__(**kwargs)
        self.gold = gold
        self.sentences1 = [sentences1[i] for (i, j) in self.gold]
        self.sentences2 = sentences2

        self.batch_size = batch_size

    def __call__(self, model):
        scores = self.compute_metrics(model)
        return scores

    def compute_metrics(self, model):
        # Compute embeddings
        sentences = list(set(self.sentences1 + self.sentences2))
        logger.info(f"Encoding {len(sentences)} sentences...")
        embeddings = model.encode(sentences, batch_size=self.batch_size)
        emb_dict = {sent: emb for sent, emb in zip(sentences, embeddings)}
        embeddings1 = np.asarray([emb_dict[sent] for sent in self.sentences1])
        embeddings2 = np.asarray([emb_dict[sent] for sent in self.sentences2])

        # Find nearest neighbors
        logger.info("Finding nearest neighbors...")
        nearest_neighbors = self._similarity_search(embeddings1, embeddings2, top_k=1)

        # Compute errors
        logger.info("Computing metrics...")
        labels = []
        predictions = []
        for i, x in enumerate(nearest_neighbors):
            j = x[0]["corpus_id"]
            predictions.append(j)
            labels.append(self.gold[i][1])

        scores = {
            "precision": precision_score(labels, predictions, average="weighted"),
            "recall": recall_score(labels, predictions, average="weighted"),
            "f1": f1_score(labels, predictions, average="weighted"),
            "accuracy": accuracy_score(labels, predictions),
        }
        return scores

    def _similarity_search(
        self,
        query_embeddings,
        corpus_embeddings,
        query_chunk_size=100,
        corpus_chunk_size=500000,
        top_k=10,
        score_function=cos_sim,
    ):
        """
        This function performs a cosine similarity search between a list of query embeddings  and a list of corpus embeddings.
        It can be used for Information Retrieval / Semantic Search for corpora up to about 1 Million entries.
        :param query_embeddings: A 2 dimensional tensor with the query embeddings.
        :param corpus_embeddings: A 2 dimensional tensor with the corpus embeddings.
        :param query_chunk_size: Process 100 queries simultaneously. Increasing that value increases the speed, but requires more memory.
        :param corpus_chunk_size: Scans the corpus 100k entries at a time. Increasing that value increases the speed, but requires more memory.
        :param top_k: Retrieve top k matching entries.
        :param score_function: Function for computing scores. By default, cosine similarity.
        :return: Returns a list with one entry for each query. Each entry is a list of dictionaries with the keys 'corpus_id' and 'score', sorted by decreasing cosine similarity scores.
        """
        query_embeddings = torch.from_numpy(query_embeddings)
        corpus_embeddings = torch.from_numpy(corpus_embeddings)
        if len(query_embeddings.shape) == 1:
            query_embeddings = query_embeddings.unsqueeze(0)
        if len(corpus_embeddings.shape) == 1:
            corpus_embeddings = corpus_embeddings.unsqueeze(0)

        # Check that corpus and queries are on the same device
        if corpus_embeddings.device != query_embeddings.device:
            query_embeddings = query_embeddings.to(corpus_embeddings.device)

        queries_result_list = [[] for _ in range(len(query_embeddings))]

        for query_start_idx in range(0, len(query_embeddings), query_chunk_size):
            # Iterate over chunks of the corpus
            for corpus_start_idx in range(0, len(corpus_embeddings), corpus_chunk_size):
                # Compute cosine similarities
                cos_scores = score_function(
                    query_embeddings[query_start_idx : query_start_idx + query_chunk_size],
                    corpus_embeddings[corpus_start_idx : corpus_start_idx + corpus_chunk_size],
                )

                # Get top-k scores
                cos_scores_top_k_values, cos_scores_top_k_idx = torch.topk(
                    cos_scores, min(top_k, len(cos_scores[0])), dim=1, largest=True, sorted=False
                )
                cos_scores_top_k_values = cos_scores_top_k_values.cpu().tolist()
                cos_scores_top_k_idx = cos_scores_top_k_idx.cpu().tolist()

                for query_itr in range(len(cos_scores)):
                    for sub_corpus_id, score in zip(
                        cos_scores_top_k_idx[query_itr], cos_scores_top_k_values[query_itr]
                    ):
                        corpus_id = corpus_start_idx + sub_corpus_id
                        query_id = query_start_idx + query_itr
                        queries_result_list[query_id].append({"corpus_id": corpus_id, "score": score})

        # Sort and strip to top_k results
        for idx in range(len(queries_result_list)):
            queries_result_list[idx] = sorted(queries_result_list[idx], key=lambda x: x["score"], reverse=True)
            queries_result_list[idx] = queries_result_list[idx][0:top_k]

        return queries_result_list
    