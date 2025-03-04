from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class IndoReligiousBitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "IndoReligiousBitextMining",
            "hf_hub_name": "kornwtp/id-religious-bitext-mining",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "mean_accuracy",
        }