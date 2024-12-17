from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class KhmerBookmebusReviews(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "KhmerBookmebusReviews",
            "hf_hub_name": "kornwtp/km-bookmebus-reviews",
            "description": "Bookmebus reviews classification for Khmer",
            "reference": "https://github.com/seanghay/awesome-khmer-language",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["km"],
            "main_score": "f1",
        }