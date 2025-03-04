from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class MalayALTBitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "MalayALTBitextMining",
            "hf_hub_name": "kornwtp/ms-alt",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["ms"],
            "main_score": "mean_accuracy",
        }