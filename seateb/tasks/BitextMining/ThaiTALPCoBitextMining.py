from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class ThaiTALPCoBitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "ThaiTALPCoBitextMining",
            "hf_hub_name": "kornwtp/th-talpco",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["th"],
            "main_score": "mean_accuracy",
        }