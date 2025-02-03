from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class TyphoonYolandaTweetsClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "TyphoonYolandaTweetsClassification",
            "hf_hub_name": "kornwtp/typhoon-yolanda-tweets-classification",
            "description": "The dataset contains annotated typhoon and disaster-related tweets in Filipino collected before, during, and after one month of Typhoon Yolanda in 2013.",
            "reference": "https://github.com/imperialite/Philippine-Languages-Online-Corpora/tree/master/Tweets/Annotated%20Yolanda",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["tl"],
            "main_score": "f1",
        }