from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class VietnameseScenarioClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "VietnameseScenarioClassification",
            "hf_hub_name": "kornwtp/vi-scenario-classification",
            "description": "Massive scenario classification from MTEB.",
            "reference": "https://huggingface.co/datasets/mteb/amazon_massive_scenario",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["vi"],
            "main_score": "f1",
        }