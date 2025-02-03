from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class ThaiCyberbullyingLGBTClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "ThaiCyberbullyingLGBTClassification",
            "hf_hub_name": "kornwtp/thai-cyberbullying-lgbt-classification",
            "description": "Thai text classification",
            "reference": "https://github.com/tiya1012/thai_cyberbullying_lgbt",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["th"],
            "main_score": "f1",
        }