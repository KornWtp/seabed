from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class KhmerALTBitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "KhmerALTBitextMining",
            "hf_hub_name": "kornwtp/km-alt",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["km"],
            "main_score": "mean_accuracy",
        }