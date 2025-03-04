from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class ThaiSoftwareDocumentationBitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "ThaiSoftwareDocumentationBitextMining",
            "hf_hub_name": "kornwtp/th-software-documentation",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["th"],
            "main_score": "mean_accuracy",
        }