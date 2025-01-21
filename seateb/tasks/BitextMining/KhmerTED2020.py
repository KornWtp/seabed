from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class KhmerTED2020(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "KhmerTED2020BitextMining",
            "hf_hub_name": "kornwtp/km-ted2020",
            "description": "Parallel sentences in English and their corresponding sentences in Khmer.",
            "reference": "https://opus.nlpl.eu",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["km"],
            "main_score": "mean_accuracy",
        }