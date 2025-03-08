import logging
from collections import defaultdict
import pandas as pd

from ..evaluation.evaluators import QARetrievalEvaluator
from .AbsTask import AbsTask


class AbsTaskInstructionRetrieval(AbsTask):
    """
    Abstract class for AbsTaskInstructionRetrieval

    The similarity between the query and document is computed, and the results are ranked. 
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def evaluate(self, model, prompts, split="test", **kwargs):
        if not self.data_loaded:
            self.load_data()
        

        data_split = self.dataset[split]
        queries = data_split["instruction"]
        documents = list(set(data_split["context"]))
        doc2idx = {d: i for i, d in enumerate(documents)}

        # Map index of query to set of relevant context documents
        relevant_docs = {idx: set([doc2idx[data["context"]]]) for idx, data in enumerate(data_split)}

        
        if prompts is not None:
            queries, documents = prompts(self.description['type'], self.description['name'], [queries, documents])

        # Assign IDs to queries and context documents
        queries = dict(enumerate(queries))
        corpus = dict(enumerate(documents))

        evaluator = QARetrievalEvaluator(queries, corpus, relevant_docs)
        scores = evaluator.compute_metrices(model)

        return scores
