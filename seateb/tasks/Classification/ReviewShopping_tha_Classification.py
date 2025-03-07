from ...abstasks.AbsTaskClassification import AbsTaskClassification


class ReviewShopping_tha_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "ReviewShopping_tha_Classification",
            "hf_hub_name": "kornwtp/review-shopping-tha-classification",
            "description": "Thai text classification",
            "reference": "https://github.com/PyThaiNLP/thai-sentiment-analysis-dataset",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["tha"],
            "main_score": "f1",
        }