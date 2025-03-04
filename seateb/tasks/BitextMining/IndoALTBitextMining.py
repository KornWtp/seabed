from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class IndoALTBitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "IndoALTBitextMining",
            "hf_hub_name": "kornwtp/id-alt",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["id"],
            "main_score": "mean_accuracy",
        }