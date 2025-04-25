from ...abstasks.AbsTaskClassification import AbsTaskClassification


class NewsSentiment_zsm_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "NewsSentiment_zsm_Classification",
            "hf_hub_name": "kornwtp/news-sentiment-zsm-classification",
            "description": "Malay news sentiment classification",
            "reference": "https://github.com/mesolitica/malaysian-dataset",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["zsm"],
            "main_score": "f1",
        }