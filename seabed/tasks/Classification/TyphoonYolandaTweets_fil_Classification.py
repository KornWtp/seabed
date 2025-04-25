from ...abstasks.AbsTaskClassification import AbsTaskClassification


class TyphoonYolandaTweets_fil_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "TyphoonYolandaTweets_fil_Classification",
            "hf_hub_name": "kornwtp/typhoon-yolanda-tweets-fil-classification",
            "description": "The dataset contains annotated typhoon and disaster-related tweets in Filipino collected before, during, and after one month of Typhoon Yolanda in 2013.",
            "reference": "https://github.com/imperialite/Philippine-Languages-Online-Corpora/tree/master/Tweets/Annotated%20Yolanda",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["fil"],
            "main_score": "f1",
        }