from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class TagalogScenarioClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "TagalogScenarioTextClassification",
            "hf_hub_name": "kornwtp/tl-scenario-classification",
            "description": "Massive scenario classification from MTEB.",
            "reference": "https://huggingface.co/datasets/mteb/amazon_massive_scenario",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["tl"],
            "main_score": "f1",
        }