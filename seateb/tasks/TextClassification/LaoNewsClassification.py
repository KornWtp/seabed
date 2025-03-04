from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class LaoNewsClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "LaoNewsClassification",
            "hf_hub_name": "kornwtp/lo-news-classification",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["lo"],
            "main_score": "f1",
        }