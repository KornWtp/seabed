from ...abstasks.AbsTaskClassification import AbsTaskClassification


class ShopeeReviews_fil_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "ShopeeReviews_fil_Classification",
            "hf_hub_name": "kornwtp/shopee-reviews-fil-classification",
            "description": "Shopee reviews star classification in Tagalog language.",
            "reference": "https://huggingface.co/datasets/scaredmeow/shopee-reviews-tl-stars",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["fil"],
            "main_score": "f1",
        }