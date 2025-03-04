from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class LaoALTBitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "LaoALTBitextMining",
            "hf_hub_name": "kornwtp/lo-alt",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["lo"],
            "main_score": "mean_accuracy",
        }