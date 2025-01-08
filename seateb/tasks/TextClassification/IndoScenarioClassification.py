from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class IndoScenarioClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "IndoScenarioTextClassification",
            "hf_hub_name": "kornwtp/id-scenario-classification",
            "description": "Massive scenario classification from MTEB.",
            "reference": "https://huggingface.co/datasets/mteb/amazon_massive_scenario",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "f1",
        }