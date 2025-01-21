from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class ThaiTED2020(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "ThaiTED2020BitextMining",
            "hf_hub_name": "kornwtp/th-ted2020",
            "description": "Parallel sentences in English and their corresponding sentences in Thai.",
            "reference": "https://opus.nlpl.eu",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["th"],
            "main_score": "mean_accuracy",
        }