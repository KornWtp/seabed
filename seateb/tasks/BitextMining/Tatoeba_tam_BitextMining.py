from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class Tatoeba_tam_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "Tatoeba_tam_BitextMining",
            "hf_hub_name": "kornwtp/tatoeba-tam-bitextmining",
            "description": "Parallel sentences in English and their corresponding sentences in Tamil.",
            "reference": "https://opus.nlpl.eu",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["tam"],
            "main_score": "f1",
        }