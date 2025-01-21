from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class IndoTED2020(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "IndoTED2020BitextMining",
            "hf_hub_name": "kornwtp/id-ted2020",
            "description": "Parallel sentences in English and their corresponding sentences in Indonesian.",
            "reference": "https://opus.nlpl.eu",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["id"],
            "main_score": "mean_accuracy",
        }