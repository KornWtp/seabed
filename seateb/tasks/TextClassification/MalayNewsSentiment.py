from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class MalayNewsSentiment(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "MalayNewsSentiment",
            "hf_hub_name": "kornwtp/ms-news-sentiment",
            "description": "Malay news sentiment classification",
            "reference": "https://github.com/mesolitica/malaysian-dataset",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["ms"],
            "main_score": "f1",
        }