from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class FilipinoLazadaReviewClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "FilipinoLazadaReviewClassification",
            "hf_hub_name": "kornwtp/filipino-lazada-review-classification",
            "description": "Filipino-Tagalog Product Reviews Sentiment Analysis This is a machine learning dataset that can be used to analyze the sentiment of product reviews in Filipino-Tagalog.",
            "reference": "https://github.com/EricEchemane/Filipino-Tagalog-Product-Reviews-Sentiment-Analysis",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["tl"],
            "main_score": "f1",
        }