from ...abstasks.AbsTaskClassification import AbsTaskClassification


class Tweets_zsm_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "Tweets_zsm_Classification",
            "hf_hub_name": "kornwtp/tweets-zsm-classification",
            "description": "This tweet data was extracted from tweets in Malaysia based on keywords social distancing and physical distancing.",
            "reference": "https://github.com/sarahjuan/malaysia-tweets-with-sentiment-labels",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["zsm"],
            "main_score": "f1",
        }