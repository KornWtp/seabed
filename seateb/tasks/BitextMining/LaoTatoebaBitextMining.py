from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class LaoTatoebaBitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "LaoTatoebaBitextMining",
            "hf_hub_name": "kornwtp/lo-tatoeba",
            "description": "Parallel sentences in English and their corresponding sentences in Lao.",
            "reference": "https://opus.nlpl.eu",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["lo"],
            "main_score": "f1",
        }