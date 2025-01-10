import logging

import numpy as np

from .Evaluator import Evaluator

logger = logging.getLogger(__name__)


class QARetrievalEvaluator(Evaluator):
    """
    Evaluate a model based on the similarity of the embeddings and retrieving relevant answers from corpus based on input queries.

    The returned scores include Precision@1, Precision@5, Precision@10, and MRR.
    :param question_id: The id of queries
    :param questions: The sentence of queries
    :param doc_context_id: The id of documents
    :param doc_context: The context of documents
    :param batch_size: Batch size used to compute embeddings
    :param write_csv: Write results to a CSV file
    """

    def __init__(
        self, question_id, questions, doc_context_id, doc_context, batch_size=32, **kwargs
    ):
        super().__init__(**kwargs)
        self.question_id = question_id
        self.questions = questions
        self.doc_context_id = doc_context_id
        self.doc_context = doc_context
        self.batch_size = batch_size


    def __call__(self, model):
        scores = self.compute_metrics(model)
    
        return scores

    def compute_metrics(self, model):
        logger.info(f"Encoding {len(self.doc_context)} documents...")
        doc_context_encoded = model.encode(self.doc_context, convert_to_numpy=True, normalize_embeddings=True)
        logger.info(f"Encoding {len(self.questions)} questions...")
        question_encoded = model.encode(self.questions, convert_to_numpy=True, normalize_embeddings=True)
        
        top_1 = 0 
        top_5 = 0 
        top_10 = 0
        mrr_score = 0
        mrr_rank = 10
        context_id = np.array(self.doc_context_id)
        sim_score = np.inner(question_encoded, doc_context_encoded)
        status_bar = enumerate(sim_score)
        for idx, sim in status_bar:
            index = np.argsort(sim)[::-1]
            index_edit = [context_id[x] for x in index]
            idx_search = list(index_edit).index(self.question_id[idx])
            if idx_search == 0:
                top_1 += 1
                top_5 += 1
                top_10 += 1
            elif idx_search < 5:
                top_5 += 1
                top_10 += 1
            elif idx_search < 10:
                top_10 += 1  
            if idx_search < mrr_rank:
                mrr_score += (1 / (idx_search + 1))
        
        precision_1 = round(top_1 / len(question_encoded), 4)
        precision_5 = round(top_5 / len(question_encoded), 4)
        precision_10 = round(top_10 / len(question_encoded), 4)
        mrr_score = round(mrr_score / len(question_encoded), 4)

        metrics = {
            "P@1": precision_1,
            "P@5": precision_5,
            "P@10": precision_10,
            "MRR": mrr_score,
        }
        
        return metrics


class MIRACLRetrievalEvaluator(Evaluator):
    """
    Evaluate a model based on the similarity of the embeddings and retrieving relevant answers from corpus based on input queries.

    The returned scores include Precision@1, Precision@5, Precision@10, and MRR.
    :param doc_context: The context of documents
    :param answers: The answer of queries
    :param questions: The sentence of queries
    :param batch_size: Batch size used to compute embeddings
    :param write_csv: Write results to a CSV file
    """

    def __init__(
        self, doc_context, answers, questions, batch_size=32, **kwargs
    ):
        super().__init__(**kwargs)
        self.doc_context = doc_context
        self.answers = answers
        self.questions = questions
        self.batch_size = batch_size


    def __call__(self, model):
        scores = self.compute_metrics(model)
    
        return scores

    def compute_metrics(self, model):
        logger.info(f"Encoding {len(self.doc_context)} documents...")
        doc_context_encoded = model.encode(self.doc_context, convert_to_numpy=True, normalize_embeddings=True)
        logger.info(f"Encoding {len(self.questions)} questions...")
        question_encoded = model.encode(self.questions, convert_to_numpy=True, normalize_embeddings=True)

        top_1 = 0 
        top_5 = 0 
        top_10 = 0
        mrr_score = 0
        mrr_rank = 10
        sim_score = np.inner(question_encoded, doc_context_encoded)
        status_bar = enumerate(sim_score)
        for idx, sim in status_bar:
            index = np.argsort(sim)[::-1]
            
            if "passage" in self.doc_context[0]:
                self.doc_context = [ex.replace("passage:", "").strip() for ex in self.doc_context]

            doc_sorted = [self.doc_context[i] for i in index]
            answer_idx = [doc_sorted.index(a) for a in self.answers[idx]] # cal index for each answer
            final_idx_search = min(answer_idx) # since we have multiple answers, we find the min index! 
            if final_idx_search == 0:
                top_1 += 1
                top_5 += 1
                top_10 += 1
            elif final_idx_search < 5:
                top_5 += 1
                top_10 += 1
            elif final_idx_search < 10:
                top_10 += 1  
            if final_idx_search < mrr_rank:
                mrr_score += (1 / (final_idx_search + 1))

        precision_1 = round(top_1 / len(question_encoded), 4)
        precision_5 = round(top_5 / len(question_encoded), 4)
        precision_10 = round(top_10 / len(question_encoded), 4)
        mrr_score = round(mrr_score / len(question_encoded), 4)
        
        metrics = {
            "P@1": precision_1,
            "P@5": precision_5,
            "P@10": precision_10,
            "MRR": mrr_score,
        }
        
        return metrics
