from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class KhineMyanmarNewsClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "KhineMyanmarNewsClassification",
            "hf_hub_name": "kornwtp/Khine-myanmar-news-classification",
            "description": "Myanmar news corpus is intended for training and evaluation of text classification tasks for the Myanmar language.",
            "reference": "https://github.com/ayehninnkhine/MyanmarNewsClassificationSystem",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["my"],
            "main_score": "f1",
        }