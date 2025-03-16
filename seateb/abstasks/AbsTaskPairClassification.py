import logging
from collections import defaultdict

from ..evaluation.evaluators import PairClassificationEvaluator
from .AbsTask import AbsTask


class AbsTaskPairClassification(AbsTask):
    """
    Abstract class for PairClassificationTasks
    The similarity is computed between pairs and the results are ranked. Average precision
    is computed to measure how well the methods can be used for pairwise pair classification.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def evaluate(self, model, prompts, split="test", **kwargs):
        if not self.data_loaded:
            self.load_data()

        data_split = self.dataset[split]

        if prompts is not None:
            data_split = prompts(self.description['type'], self.description['name'], data_split)
        
        logging.getLogger("sentence_transformers.evaluation.PairClassificationEvaluator").setLevel(logging.WARN)
        evaluator = PairClassificationEvaluator(
            data_split["sentence1"], data_split["sentence2"], data_split["label"], **kwargs
        )
        scores = evaluator.compute_metrics(model)

        # Compute max
        max_scores = defaultdict(list)
        for sim_fct in scores:
            for metric in ["accuracy", "f1", "ap"]:
                max_scores[metric].append(scores[sim_fct][metric])

        for metric in max_scores:
            max_scores[metric] = max(max_scores[metric])

        scores["max"] = dict(max_scores)
        
       
        return scores