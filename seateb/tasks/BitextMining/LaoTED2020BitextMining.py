from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class LaoTED2020BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "LaoTED2020BitextMining",
            "hf_hub_name": "kornwtp/lo-ted2020",
            "description": "Parallel sentences in English and their corresponding sentences in Lao.",
            "reference": "https://opus.nlpl.eu",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["lo"],
            "main_score": "f1",
        }