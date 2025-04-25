from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class Tatoeba_tha_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "Tatoeba_tha_BitextMining",
            "hf_hub_name": "kornwtp/tatoeba-tha-bitextmining",
            "description": "Parallel sentences in English and their corresponding sentences in Thai.",
            "reference": "https://opus.nlpl.eu",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["tha"],
            "main_score": "f1",
        }