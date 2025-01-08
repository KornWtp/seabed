from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class TamilmurasuNewsClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "TamilmurasuNewsTextClassification",
            "hf_hub_name": "kornwtp/tamilmurasu-news-classification",
            "description": "News articles classification from Tamil newspaper.",
            "reference": "https://www.kaggle.com/datasets/vijayabhaskar96/tamil-news-classification-dataset-tamilmurasu",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["tl"],
            "main_score": "f1",
        }