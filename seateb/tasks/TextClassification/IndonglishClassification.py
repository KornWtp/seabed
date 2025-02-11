from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class IndonglishClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "IndonglishClassification",
            "hf_hub_name": "kornwtp/indonglish-classification",
            "description": "Indonglish-dataset was constructed based on keywords derived from the sociolinguistic phenomenon observed among teenagers in South Jakarta.",
            "reference": "https://github.com/laksmitawidya/indonglish-dataset",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "f1",
        }