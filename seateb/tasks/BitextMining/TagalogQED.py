from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class TagalogQED(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "TagalogQED",
            "hf_hub_name": "kornwtp/tl-qed",
            "description": "Parallel sentences in English and their corresponding sentences in Tagalog.",
            "reference": "https://opus.nlpl.eu",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["tl"],
            "main_score": "mean_accuracy",
        }