import logging

from contextlib import nullcontext
import numpy as np
import torch
from sentence_transformers.util import pytorch_cos_sim

from .Evaluator import Evaluator

logger = logging.getLogger(__name__)


class CrossLingualRetrievalEvaluator(Evaluator):
    """
    Evaluate a model based on the similarity of the embeddings by calculating the accuracy of identifying similar and
    dissimilar sentences.
    The metrics are the cosine similarity
    The returned score is the accuracy with a specified metric.
    :param sentences1: The source language column of sentences
    :param sentences2: The target language column of sentences
    :param name: Name for the output
    :param batch_size: Batch size used to compute embeddings
    :param truncate_dim: The dimension to truncate sentence embeddings to. If None, the model's
        current truncation dimension will be used. Defaults to None.
    :param print_wrong_matches: Whether to print incorrect matches. Defaults to False.
    :param write_csv: Write results to a CSV file
    """

    def __init__(
        self, sentences1, sentences2, batch_size=32, limit=None, print_wrong_matches=False, truncate_dim=None, **kwargs
    ):
        super().__init__(**kwargs)
        if limit:
            sentences1 = sentences1[:limit]
            sentences2 = sentences2[:limit]
        self.sentences1 = sentences1
        self.sentences2 = sentences2
        self.batch_size = batch_size
        self.truncate_dim = truncate_dim
        self.print_wrong_matches = print_wrong_matches
        
        assert len(self.sentences1) == len(self.sentences2)


    def __call__(self, model):
        scores = self.compute_metrics(model)
        
        # Main score is the max of Average Precision (AP)
        main_score = max(scores[short_name]["mean_accuracy"] for short_name in scores)
        scores["main_score"] = main_score
        return scores

    def compute_metrics(self, model):

        with nullcontext() if self.truncate_dim is None else model.truncate_sentence_embeddings(self.truncate_dim):
            self.sentences1 = self.sentences1[:1000]
            self.sentences2 = self.sentences2[:1000]
            sentences = list(set(self.sentences1 + self.sentences2))
            logger.info(f"Encoding {len(sentences)} sentences...")
            embeddings = model.encode(sentences, batch_size=self.batch_size, convert_to_numpy=False)
            emb_dict = {sent: emb for sent, emb in zip(sentences, embeddings)}
            embeddings1 = torch.stack([emb_dict[sent] for sent in self.sentences1])
            embeddings2 = torch.stack([emb_dict[sent] for sent in self.sentences2])

        cos_sims = pytorch_cos_sim(embeddings1, embeddings2).detach().cpu().numpy()

        correct_src2trg = 0
        correct_trg2src = 0

        for i in range(len(cos_sims)):
            max_idx = np.argmax(cos_sims[i])

            if i == max_idx:
                correct_src2trg += 1
            elif self.print_wrong_matches:
                print("\nIncorrect  : Source", i, "is most similar to target", max_idx, "instead of target", i)
                print("Source     :", self.sentences1[i])
                print("Pred Target:", self.sentences2[max_idx], f"(Score: {cos_sims[i][max_idx]:.4f})")
                print("True Target:", self.sentences2[i], f"(Score: {cos_sims[i][i]:.4f})")

                results = enumerate(cos_sims[i])
                results = sorted(results, key=lambda x: x[1], reverse=True)
                for idx, score in results[:5]:
                    print("\t", idx, f"(Score: {score:.4f})", self.sentences2[idx])

        cos_sims = cos_sims.T
        for i in range(len(cos_sims)):
            max_idx = np.argmax(cos_sims[i])
            if i == max_idx:
                correct_trg2src += 1

        acc_src2trg = correct_src2trg / len(cos_sims)
        acc_trg2src = correct_trg2src / len(cos_sims)

        logger.info(f"Accuracy src2trg: {acc_src2trg * 100:.2f}")
        logger.info(f"Accuracy trg2src: {acc_trg2src * 100:.2f}")

        metrics = {
            "src2trg_accuracy": acc_src2trg,
            "trg2src_accuracy": acc_trg2src,
            "mean_accuracy": (acc_src2trg + acc_trg2src) / 2,
        }
        
        return metrics

    