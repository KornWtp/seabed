from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class IndoTALPCoBitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "IndoTALPCoBitextMining",
            "hf_hub_name": "kornwtp/id-talpco",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["id"],
            "main_score": "mean_accuracy",
        }