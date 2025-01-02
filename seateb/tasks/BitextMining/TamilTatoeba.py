from ...abstasks.AbsTaskCrossLingualRetrieval import AbsTaskCrossLingualRetrieval


class TamilTatoeba(AbsTaskCrossLingualRetrieval):
    @property
    def description(self):
        return {
            "name": "TamilTatoeba",
            "hf_hub_name": "kornwtp/ta-tatoeba",
            "description": "Parallel sentences in English and their corresponding sentences in Tamil.",
            "reference": "https://opus.nlpl.eu",
            "category": "s2s",
            "type": "CrossLingualRetrieval",
            "eval_splits": ["train"],
            "eval_langs": ["ta"],
            "main_score": "mean_accuracy",
        }