from ...abstasks.AbsTaskCrossLingualRetrieval import AbsTaskCrossLingualRetrieval


class TagalogTED2020(AbsTaskCrossLingualRetrieval):
    @property
    def description(self):
        return {
            "name": "TagalogTED2020",
            "hf_hub_name": "kornwtp/fil-ted2020",
            "description": "Parallel sentences in English and their corresponding sentences in Tagalog.",
            "reference": "https://opus.nlpl.eu",
            "category": "s2s",
            "type": "CrossLingualRetrieval",
            "eval_splits": ["train"],
            "eval_langs": ["fil"],
            "main_score": "mean_accuracy",
        }