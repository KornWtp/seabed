from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class IndoKaroneseClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "IndoKaroneseClassification",
            "hf_hub_name": "kornwtp/id-karonese-classification",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "f1",
        }