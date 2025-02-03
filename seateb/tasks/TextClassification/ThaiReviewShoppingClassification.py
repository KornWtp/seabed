from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class ThaiReviewShoppingClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "ThaiReviewShoppingClassification",
            "hf_hub_name": "kornwtp/review-shopping-classification",
            "description": "Thai text classification",
            "reference": "https://github.com/PyThaiNLP/thai-sentiment-analysis-dataset",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["th"],
            "main_score": "f1",
        }