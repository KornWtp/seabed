from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class ThaiLimeSodaClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "ThaiLimeSodaClassification",
            "hf_hub_name": "kornwtp/lime-soda-classification",
            "description": "Thai fake news dataset in the healthcare domain",
            "reference": "https://github.com/byinth/LimeSoda",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["th"],
            "main_score": "f1",
        }