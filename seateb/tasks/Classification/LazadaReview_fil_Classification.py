from ...abstasks.AbsTaskClassification import AbsTaskClassification


class LazadaReview_fil_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "LazadaReview_fil_Classification",
            "hf_hub_name": "kornwtp/lazada-review-fil-classification",
            "description": "Filipino-Tagalog Product Reviews Sentiment Analysis This is a machine learning dataset that can be used to analyze the sentiment of product reviews in Filipino-Tagalog.",
            "reference": "https://github.com/EricEchemane/Filipino-Tagalog-Product-Reviews-Sentiment-Analysis",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["fil"],
            "main_score": "f1",
        }