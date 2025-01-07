from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class KhmerScenarioClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "KhmerScenarioTextClassification",
            "hf_hub_name": "kornwtp/km-scenario-classification",
            "description": "Massive scenario classification from MTEB.",
            "reference": "https://huggingface.co/datasets/mteb/amazon_massive_scenario",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["km"],
            "main_score": "f1",
        }