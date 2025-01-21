from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class MalayTED2020(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "MalayTED2020BitextMining",
            "hf_hub_name": "kornwtp/ms-ted2020",
            "description": "Parallel sentences in English and their corresponding sentences in Malay.",
            "reference": "https://opus.nlpl.eu",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["ms"],
            "main_score": "mean_accuracy",
        }