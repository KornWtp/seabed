from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class MyanmarNewsClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "MyanmarNewsClassification",
            "hf_hub_name": "kornwtp/myanmar-news-classification",
            "description": "Myanmar news corpus is intended for training and evaluation of text classification tasks for the Myanmar language.",
            "reference": "https://huggingface.co/datasets/mteb/MyanmarNews",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["my"],
            "main_score": "f1",
        }