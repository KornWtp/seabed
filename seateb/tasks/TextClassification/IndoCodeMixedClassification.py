from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class IndoCodeMixedClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "IndoCodeMixedClassification",
            "hf_hub_name": "kornwtp/id-code-mixed-classification",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "f1",
        }