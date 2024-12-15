from ...abstasks.AbsTaskCrossLingualRetrieval import AbsTaskCrossLingualRetrieval


class ThaiTED2020(AbsTaskCrossLingualRetrieval):
    @property
    def description(self):
        return {
            "name": "ThaiTED2020",
            "hf_hub_name": "kornwtp/th-ted2020",
            "description": "Parallel sentences in English and their corresponding sentences in Thai.",
            "reference": "https://opus.nlpl.eu",
            "category": "s2s",
            "type": "CrossLingualRetrieval",
            "eval_splits": ["train"],
            "eval_langs": ["th"],
            "main_score": "mean_accuracy",
        }