from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class TamilIntentClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "TamilIntentTextClassification",
            "hf_hub_name": "kornwtp/tl-intent-classification",
            "description": "Massive intent classification from MTEB.",
            "reference": "https://huggingface.co/datasets/mteb/amazon_massive_intent",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["tl"],
            "main_score": "f1",
        }