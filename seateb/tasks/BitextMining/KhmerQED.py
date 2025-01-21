from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class KhmerQED(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "KhmerQEDBitextMining",
            "hf_hub_name": "kornwtp/km-qed",
            "description": "Parallel sentences in English and their corresponding sentences in Khmer.",
            "reference": "https://opus.nlpl.eu",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["km"],
            "main_score": "mean_accuracy",
        }