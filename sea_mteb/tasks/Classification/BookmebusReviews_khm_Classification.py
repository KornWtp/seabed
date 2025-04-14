from ...abstasks.AbsTaskClassification import AbsTaskClassification


class BookmebusReviews_khm_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "BookmebusReviews_khm_Classification",
            "hf_hub_name": "kornwtp/bookmebus-reviews-khm-classification",
            "description": "Bookmebus reviews classification for Khmer",
            "reference": "https://github.com/seanghay/awesome-khmer-language",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["khm"],
            "main_score": "f1",
        }