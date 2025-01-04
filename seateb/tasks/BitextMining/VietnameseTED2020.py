from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class VietnameseTED2020(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "VietnameseTED2020",
            "hf_hub_name": "kornwtp/vi-ted2020",
            "description": "Parallel sentences in English and their corresponding sentences in Vitenamese.",
            "reference": "https://opus.nlpl.eu",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["vi"],
            "main_score": "mean_accuracy",
        }