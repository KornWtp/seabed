from ...abstasks.AbsTaskClassification import AbsTaskClassification


class News_khm_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "News_khm_Classification",
            "hf_hub_name": "kornwtp/news-khm-classification",
            "description": "Khmer news article on traffic accident",
            "reference": "https://github.com/phylypo/khmer-text-data",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["khm"],
            "main_score": "f1",
        }