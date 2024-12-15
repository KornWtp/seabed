from ...abstasks.AbsTaskCrossLingualRetrieval import AbsTaskCrossLingualRetrieval


class IndoTatoeba(AbsTaskCrossLingualRetrieval):
    @property
    def description(self):
        return {
            "name": "IndoTatoeba",
            "hf_hub_name": "kornwtp/id-tatoeba",
            "description": "Parallel sentences in English and their corresponding sentences in Indonesian.",
            "reference": "https://opus.nlpl.eu",
            "category": "s2s",
            "type": "CrossLingualRetrieval",
            "eval_splits": ["train"],
            "eval_langs": ["id"],
            "main_score": "mean_accuracy",
        }