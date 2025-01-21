from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class BurmeseQEDBitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "BurmeseQEDBitextMining",
            "hf_hub_name": "kornwtp/my-qed",
            "description": "Parallel sentences in English and their corresponding sentences in Burmese.",
            "reference": "https://opus.nlpl.eu",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["my"],
            "main_score": "f1",
        }