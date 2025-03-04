from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class VietnameseTALPCoBitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "VietnameseTALPCoBitextMining",
            "hf_hub_name": "kornwtp/vi-talpco",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["vi"],
            "main_score": "mean_accuracy",
        }