from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class VietnameseSpamReviewsClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "VietnameseSpamReviewsClassification",
            "hf_hub_name": "kornwtp/vi-spam-reviews-classification",
            "description": "The dataset was collected from leading online shopping platforms in Vietnam. Some of the most recent selling products for each product category were selected and up to 15 reviews per product were collected.",
            "reference": "https://github.com/sonlam1102/vispamdetection",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["vi"],
            "main_score": "f1",
        }