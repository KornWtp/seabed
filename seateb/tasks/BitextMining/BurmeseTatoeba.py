from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class BurmeseTatoebaBitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "BurmeseTatoebaBitextMining",
            "hf_hub_name": "kornwtp/my-tatoeba",
            "description": "Parallel sentences in English and their corresponding sentences in Burmese.",
            "reference": "https://opus.nlpl.eu",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["my"],
            "main_score": "f1",
        }