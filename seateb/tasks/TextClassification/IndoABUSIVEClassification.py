from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class IndoABUSIVEClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "IndoABUSIVEClassification",
            "hf_hub_name": "kornwtp/id-abusive-classification",
            "description": "The ID_ABUSIVE dataset is collection of 2,016 informal abusive tweets in Indonesian language, designed for sentiment analysis NLP task.",
            "reference": "https://github.com/dadelani/sib-200",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "f1",
        }