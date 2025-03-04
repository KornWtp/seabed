from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class MalaySoftwareDocumentationBitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "MalaySoftwareDocumentationBitextMining",
            "hf_hub_name": "kornwtp/ms-software-documentation",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["ms"],
            "main_score": "mean_accuracy",
        }