from ...abstasks.AbsTaskCrossLingualRetrieval import AbsTaskCrossLingualRetrieval


class TagalogTatoeba(AbsTaskCrossLingualRetrieval):
    @property
    def description(self):
        return {
            "name": "TagalogTatoeba",
            "hf_hub_name": "kornwtp/tl-tatoeba",
            "description": "Parallel sentences in English and their corresponding sentences in Tagalog.",
            "reference": "https://opus.nlpl.eu",
            "category": "s2s",
            "type": "CrossLingualRetrieval",
            "eval_splits": ["train"],
            "eval_langs": ["tl"],
            "main_score": "mean_accuracy",
        }