from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class IndoNLGBitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "IndoNLGBitextMining",
            "hf_hub_name": "kornwtp/id-indonlg-bitext-mining",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "mean_accuracy",
        }