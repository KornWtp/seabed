from ...abstasks.AbsTaskClassification import AbsTaskClassification


class CyberbullyingLGBT_tha_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "CyberbullyingLGBT_tha_Classification",
            "hf_hub_name": "kornwtp/cyberbullying-lgbt-tha-classification",
            "description": "Thai text classification",
            "reference": "https://github.com/tiya1012/thai_cyberbullying_lgbt",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["tha"],
            "main_score": "f1",
        }