from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class VietnameseSoftwareDocumentationBitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "VietnameseSoftwareDocumentationBitextMining",
            "hf_hub_name": "kornwtp/vi-software-documentation",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["vi"],
            "main_score": "mean_accuracy",
        }