from ...abstasks.AbsTaskClassification import AbsTaskClassification


class MassiveScenario_fil_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "MassiveScenario_fil_Classification",
            "hf_hub_name": "kornwtp/massive-scenario-fil-classification",
            "description": "Massive scenario classification from MTEB.",
            "reference": "https://huggingface.co/datasets/mteb/amazon_massive_scenario",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["fil"],
            "main_score": "f1",
        }