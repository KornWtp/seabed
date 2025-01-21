from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class ThuraMyanmarNewsClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "ThuraMyanmarNewsClassification",
            "hf_hub_name": "kornwtp/Thura-myanmar-news-classification",
            "description": "Myanmar news corpus is intended for training and evaluation of text classification tasks for the Myanmar language.",
            "reference": "https://huggingface.co/datasets/ThuraAung1601/myanmar_news",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["my"],
            "main_score": "f1",
        }