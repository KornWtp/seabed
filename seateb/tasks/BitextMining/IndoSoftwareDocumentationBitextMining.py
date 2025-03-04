from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class IndoSoftwareDocumentationBitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "IndoSoftwareDocumentationBitextMining",
            "hf_hub_name": "kornwtp/id-software-documentation",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["id"],
            "main_score": "mean_accuracy",
        }