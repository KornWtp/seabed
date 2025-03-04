from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class BurmeseTALPCoBitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "BurmeseTALPCoBitextMining",
            "hf_hub_name": "kornwtp/my-talpco",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["my"],
            "main_score": "mean_accuracy",
        }