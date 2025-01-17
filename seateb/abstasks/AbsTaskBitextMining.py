from ..evaluation.evaluators import BitextMiningEvaluator
from .AbsTask import AbsTask


class AbsTaskBitextMining(AbsTask):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def evaluate(self, model, prompts, split, **kwargs):
        if not self.data_loaded:
            self.load_data()

        if self.is_crosslingual:
            scores = {}
            for lang in self.dataset:
                print(f"\nTask: {self.description['name']}, split: {split}, language: {lang}. Running...")
                data_split = self.dataset[lang][split]
                
                if prompts is not None:
                    data_split = prompts(self.description['type'], self.description['name'], data_split)
                
                scores[lang] = self._evaluate_split(model, data_split, **kwargs)
        else:
            print(f"\nTask: {self.description['name']}, split: {split}. Running...")
            data_split = self.dataset[split]

            if prompts is not None:
                data_split = prompts(self.description['type'], self.description['name'], data_split)

            scores = self._evaluate_split(model, data_split, **kwargs)

        return scores

    def _evaluate_split(self, model, data_split, **kwargs):
        if len(data_split["source"]) == 1:
            sentence1 = data_split["source"][0]
        else:
            sentence1 = data_split["source"]
        if len(data_split["target"]) == 1:
            sentence2 = data_split["target"][0]
        else:
            sentence2 = data_split["target"]

        if not ("gold" in data_split.features):
            assert len(sentence1) == len(sentence2), "Wrong dataset format"
            n = len(sentence1)
            gold = list(zip(range(n), range(n)))
        else:
            gold = data_split["gold"]
            if len(gold) == 1:
                gold = gold[0]
            # MTEB currently only loads GOLD labels for BUCC, which is 1-indexed
            # If a 2nd 0-indexed dataset is added, it'd be cleaner to update BUCC on the Hub to be 0-indexed
            gold = [(i - 1, j - 1) for (i, j) in gold]
            assert all(
                [(i>0) and (j>0) for i,j in gold]
            ), "Found negative gold indices. This may be caused by MTEB expecting 1-indexed gold labels."
        
        evaluator = BitextMiningEvaluator(sentence1, sentence2, gold, **kwargs)
        metrics = evaluator(model)
        return metrics