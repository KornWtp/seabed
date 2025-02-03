from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class MalayTweetsClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "MalayTweetsClassification",
            "hf_hub_name": "kornwtp/ms-tweets-classification",
            "description": "This tweet data was extracted from tweets in Malaysia based on keywords social distancing and physical distancing.",
            "reference": "https://github.com/sarahjuan/malaysia-tweets-with-sentiment-labels",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["ms"],
            "main_score": "f1",
        }