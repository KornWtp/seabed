from ...abstasks.AbsTaskCrossLingualRetrieval import AbsTaskCrossLingualRetrieval


class MalayTED2020(AbsTaskCrossLingualRetrieval):
    @property
    def description(self):
        return {
            "name": "MalayTED2020",
            "hf_hub_name": "kornwtp/ms-ted2020",
            "description": "Parallel sentences in English and their corresponding sentences in Malay.",
            "reference": "https://opus.nlpl.eu",
            "category": "s2s",
            "type": "CrossLingualRetrieval",
            "eval_splits": ["train"],
            "eval_langs": ["ms"],
            "main_score": "mean_accuracy",
        }