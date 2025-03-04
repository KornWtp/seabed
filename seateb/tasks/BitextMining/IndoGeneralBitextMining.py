from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class IndoGeneralBitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "IndoGeneralBitextMining",
            "hf_hub_name": "kornwtp/id-general-bitext-mining",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "mean_accuracy",
        }