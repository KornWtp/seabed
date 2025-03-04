from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class FilipinoALTBitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "FilipinoALTBitextMining",
            "hf_hub_name": "kornwtp/fil-alt",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["fil"],
            "main_score": "mean_accuracy",
        }