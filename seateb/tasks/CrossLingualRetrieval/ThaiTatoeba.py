from ...abstasks.AbsTaskCrossLingualRetrieval import AbsTaskCrossLingualRetrieval


class ThaiTatoeba(AbsTaskCrossLingualRetrieval):
    @property
    def description(self):
        return {
            "name": "ThaiTatoeba",
            "hf_hub_name": "kornwtp/th-tatoeba",
            "description": "Parallel sentences in English and their corresponding sentences in Thai.",
            "reference": "https://opus.nlpl.eu",
            "category": "s2s",
            "type": "CrossLingualRetrieval",
            "eval_splits": ["train"],
            "eval_langs": ["th"],
            "main_score": "mean_accuracy",
        }