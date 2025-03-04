from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class MalayTALPCoBitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "MalayTALPCoBitextMining",
            "hf_hub_name": "kornwtp/ms-talpco",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["ms"],
            "main_score": "mean_accuracy",
        }