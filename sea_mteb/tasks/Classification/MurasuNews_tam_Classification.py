from ...abstasks.AbsTaskClassification import AbsTaskClassification


class MurasuNews_tam_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "MurasuNews_tam_Classification",
            "hf_hub_name": "kornwtp/murasu-news-tam-classification",
            "description": "News articles classification from Tamil newspaper.",
            "reference": "https://www.kaggle.com/datasets/vijayabhaskar96/tamil-news-classification-dataset-tamilmurasu",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["tam"],
            "main_score": "f1",
        }