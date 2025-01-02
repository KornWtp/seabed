from ...abstasks.AbsTaskCrossLingualRetrieval import AbsTaskCrossLingualRetrieval


class MalayQED(AbsTaskCrossLingualRetrieval):
    @property
    def description(self):
        return {
            "name": "MalayQED",
            "hf_hub_name": "kornwtp/ms-qed",
            "description": "Parallel sentences in English and their corresponding sentences in Malay.",
            "reference": "https://opus.nlpl.eu",
            "category": "s2s",
            "type": "CrossLingualRetrieval",
            "eval_splits": ["train"],
            "eval_langs": ["ms"],
            "main_score": "mean_accuracy",
        }