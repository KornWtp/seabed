from ...abstasks.AbsTaskClassification import AbsTaskClassification


class ThuraMyanmarNews_mya_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "ThuraMyanmarNews_mya_Classification",
            "hf_hub_name": "kornwtp/thura-myanmar-news-mya-classification",
            "description": "Myanmar news corpus is intended for training and evaluation of text classification tasks for the Myanmar language.",
            "reference": "https://huggingface.co/datasets/ThuraAung1601/myanmar_news",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["mya"],
            "main_score": "f1",
        }
