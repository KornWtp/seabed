import logging

from ..evaluation.evaluators import ClusteringEvaluator
from .AbsTask import AbsTask
import numpy as np

logger = logging.getLogger(__name__)


class AbsTaskClustering(AbsTask):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def evaluate(self, model, prompts, split="test", **kwargs):
        if not self.data_loaded:
            self.load_data()

        if prompts is not None:
            data_split = prompts(self.description['type'], self.description['name'], self.dataset[split]["texts"])
        else:
            data_split = self.dataset[split]["texts"]

        evaluator = ClusteringEvaluator(data_split, self.dataset[split]["labels"], **kwargs)
        metrics = evaluator(model)

        v_mean = np.mean(metrics["v_measure"])
        v_std = np.std(metrics["v_measure"])
        return {"v_measure": v_mean}