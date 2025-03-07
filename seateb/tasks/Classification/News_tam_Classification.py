from ...abstasks.AbsTaskClassification import AbsTaskClassification


class News_tam_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "News_tam_Classification",
            "hf_hub_name": "kornwtp/news-tam-classification",
            "description": "News articles classification from Tamil news websites.",
            "reference": "https://www.kaggle.com/datasets/disisbig/bengali-news-dataset",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["tam"],
            "main_score": "f1",
        }