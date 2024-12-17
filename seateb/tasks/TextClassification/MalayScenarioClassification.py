from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class MalayScenarioClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "MalayScenarioClassification",
            "hf_hub_name": "kornwtp/ms-scenario-classification",
            "description": "Massive scenario classification from MTEB.",
            "reference": "https://huggingface.co/datasets/mteb/amazon_massive_scenario",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["ms"],
            "main_score": "f1",
        }