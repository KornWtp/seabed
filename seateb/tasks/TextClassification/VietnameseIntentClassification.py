from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class VietnameseIntentClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "VietnameseIntentTextClassification",
            "hf_hub_name": "kornwtp/vi-intent-classification",
            "description": "Massive intent classification from MTEB.",
            "reference": "https://huggingface.co/datasets/mteb/amazon_massive_intent",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["vi"],
            "main_score": "f1",
        }