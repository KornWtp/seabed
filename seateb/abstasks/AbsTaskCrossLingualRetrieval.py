import logging

from ..evaluation.evaluators import CrossLingualRetrievalEvaluator
from .AbsTask import AbsTask


class AbsTaskCrossLingualRetrieval(AbsTask):
    """
    Abstract class for CrossLingualRetrievalTasks
    The similarity is computed between pairs, and the results determine if vec(source) 
    has the highest similarity to vec(target). The accuracy is calculated in both directions.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def evaluate(self, model, split="test", **kwargs):
        if not self.data_loaded:
            self.load_data()
        
        data_split = self.dataset[split]
        
        evaluator = CrossLingualRetrievalEvaluator(
            data_split["source"], data_split["target"], **kwargs
        )
        scores = evaluator.compute_metrics(model)

        return scores