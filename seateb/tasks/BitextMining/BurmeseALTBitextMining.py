from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class BurmeseALTBitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "BurmeseALTBitextMining",
            "hf_hub_name": "kornwtp/my-alt",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["my"],
            "main_score": "mean_accuracy",
        }