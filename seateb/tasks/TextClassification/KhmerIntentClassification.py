from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class KhmerIntentClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "KhmerIntentTextClassification",
            "hf_hub_name": "kornwtp/km-intent-classification",
            "description": "Massive intent classification from MTEB.",
            "reference": "https://huggingface.co/datasets/mteb/amazon_massive_intent",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["km"],
            "main_score": "f1",
        }