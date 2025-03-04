from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class ThaiALTBitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "ThaiALTBitextMining",
            "hf_hub_name": "kornwtp/th-alt",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["th"],
            "main_score": "mean_accuracy",
        }