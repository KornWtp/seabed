from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class LaoQEDBitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "LaoQEDBitextMining",
            "hf_hub_name": "kornwtp/lo-qed",
            "description": "Parallel sentences in English and their corresponding sentences in Lao.",
            "reference": "https://opus.nlpl.eu",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["lo"],
            "main_score": "f1",
        }