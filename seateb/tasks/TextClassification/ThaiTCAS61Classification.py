from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class ThaiTCAS61Classification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "ThaiTCAS61Classification",
            "hf_hub_name": "kornwtp/tcas61-classification",
            "description": "Thai text classification",
            "reference": "https://github.com/PyThaiNLP/thai-sentiment-analysis-dataset",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["th"],
            "main_score": "f1",
        }