from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class IndoNewsBitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "IndoNewsBitextMining",
            "hf_hub_name": "kornwtp/id-news-bitext-mining",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "mean_accuracy",
        }