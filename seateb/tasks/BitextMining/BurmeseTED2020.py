from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class BurmeseTED2020BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "BurmeseTED2020BitextMining",
            "hf_hub_name": "kornwtp/my-ted2020",
            "description": "Parallel sentences in English and their corresponding sentences in Burmese.",
            "reference": "https://opus.nlpl.eu",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["my"],
            "main_score": "f1",
        }