from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class TagalogShopeeReviewsClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "TagalogShopeeReviewsClassification",
            "hf_hub_name": "kornwtp/tl-shopee-reviews",
            "description": "Shopee reviews star classification in Tagalog language.",
            "reference": "https://huggingface.co/datasets/scaredmeow/shopee-reviews-tl-stars",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["tl"],
            "main_score": "f1",
        }