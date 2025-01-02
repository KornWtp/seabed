from ...abstasks.AbsTaskCrossLingualRetrieval import AbsTaskCrossLingualRetrieval


class TamilTED2020(AbsTaskCrossLingualRetrieval):
    @property
    def description(self):
        return {
            "name": "TamilTED2020",
            "hf_hub_name": "kornwtp/ta-ted2020",
            "description": "Parallel sentences in English and their corresponding sentences in Tamil.",
            "reference": "https://opus.nlpl.eu",
            "category": "s2s",
            "type": "CrossLingualRetrieval",
            "eval_splits": ["train"],
            "eval_langs": ["ta"],
            "main_score": "mean_accuracy",
        }