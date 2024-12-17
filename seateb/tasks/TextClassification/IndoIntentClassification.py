from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class IndoIntentClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "IndoIntentClassification",
            "hf_hub_name": "kornwtp/id-intent-classification",
            "description": "Massive intent classification from MTEB.",
            "reference": "https://huggingface.co/datasets/mteb/amazon_massive_intent",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "f1",
        }