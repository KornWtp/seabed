from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class KhmerNewsClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "KhmerNewsTextClassification",
            "hf_hub_name": "kornwtp/km-news-article-classification",
            "description": "Khmer news article on traffic accident",
            "reference": "https://github.com/phylypo/khmer-text-data",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["km"],
            "main_score": "f1",
        }