from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class VietnameseALTBitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "VietnameseALTBitextMining",
            "hf_hub_name": "kornwtp/vi-alt",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["vi"],
            "main_score": "mean_accuracy",
        }