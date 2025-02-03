from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class VietnamesePhoATISClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "VietnamesePhoATISClassification",
            "hf_hub_name": "kornwtp/vi-phoatis-classification",
            "description": "This corpus is intent detection and slot filling dataset for Vietnamese.",
            "reference": "https://github.com/VinAIResearch/JointIDSF/",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["vi"],
            "main_score": "f1",
        }