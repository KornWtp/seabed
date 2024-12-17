from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class MalayIntentClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "MalayIntentClassification",
            "hf_hub_name": "kornwtp/ms-intent-classification",
            "description": "Massive intent classification from MTEB.",
            "reference": "https://huggingface.co/datasets/mteb/amazon_massive_intent",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["ms"],
            "main_score": "f1",
        }