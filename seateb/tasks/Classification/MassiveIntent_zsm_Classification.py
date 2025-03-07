from ...abstasks.AbsTaskClassification import AbsTaskClassification


class MassiveIntent_zsm_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "MassiveIntent_zsm_Classification",
            "hf_hub_name": "kornwtp/massive-intent-zsm-classification",
            "description": "Massive intent classification from MTEB.",
            "reference": "https://huggingface.co/datasets/mteb/amazon_massive_intent",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["zsm"],
            "main_score": "f1",
        }