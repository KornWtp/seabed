from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class ThaiDepressionClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "ThaiDepressionClassification",
            "hf_hub_name": "kornwtp/thai-depression-classification",
            "description": "Thai text classification",
            "reference": "https://huggingface.co/datasets/SEACrowd/thai_depression",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["th"],
            "main_score": "f1",
        }