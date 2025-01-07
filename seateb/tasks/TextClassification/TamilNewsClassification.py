from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class TamilNewsClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "TamilNewsTextClassification",
            "hf_hub_name": "kornwtp/ta-news-classification",
            "description": "News articles classification from Tamil news websites.",
            "reference": "https://huggingface.co/datasets/mteb/amazon_massive_intent",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["ta"],
            "main_score": "f1",
        }