from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class ThaiScenarioClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "ThaiScenarioClassification",
            "hf_hub_name": "kornwtp/th-scenario-classification",
            "description": "Massive scenario classification from MTEB.",
            "reference": "https://huggingface.co/datasets/mteb/amazon_massive_scenario",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["th"],
            "main_score": "f1",
        }