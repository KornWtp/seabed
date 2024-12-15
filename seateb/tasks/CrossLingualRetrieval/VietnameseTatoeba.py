from ...abstasks.AbsTaskCrossLingualRetrieval import AbsTaskCrossLingualRetrieval


class VietnameseTatoeba(AbsTaskCrossLingualRetrieval):
    @property
    def description(self):
        return {
            "name": "VietnameseTatoeba",
            "hf_hub_name": "kornwtp/vi-tatoeba",
            "description": "Parallel sentences in English and their corresponding sentences in Vitenamese.",
            "reference": "https://opus.nlpl.eu",
            "category": "s2s",
            "type": "CrossLingualRetrieval",
            "eval_splits": ["train"],
            "eval_langs": ["vi"],
            "main_score": "mean_accuracy",
        }