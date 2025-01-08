import logging

from ..evaluation.evaluators import BitextMiningEvaluator
from .AbsTask import AbsTask


class AbsTaskBitextMining(AbsTask):
    """
    Abstract class for BitextMiningTasks
    The similarity is computed between pairs, and the results determine if vec(source) 
    has the highest similarity to vec(target). The accuracy is calculated in both directions.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def evaluate(self, model, prompts, split="test", **kwargs):
        if not self.data_loaded:
            self.load_data()
        
        data_split = self.dataset[split]

        if prompts is not None:
            data_split = prompts(self.description['type'], self.description['name'], data_split)
        
        evaluator = BitextMiningEvaluator(
            data_split["source"], data_split["target"], **kwargs
        )
        scores = evaluator.compute_metrics(model)

        return scores