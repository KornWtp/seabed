from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class IndoIdenticBitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "IndoIdenticBitextMining",
            "hf_hub_name": "kornwtp/id-identic",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["id"],
            "main_score": "mean_accuracy",
        }