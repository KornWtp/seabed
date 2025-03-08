from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class Tatoeba_mya_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "Tatoeba_mya_BitextMining",
            "hf_hub_name": "kornwtp/tatoeba-mya-bitextmining",
            "description": "Parallel sentences in English and their corresponding sentences in Burmese.",
            "reference": "https://opus.nlpl.eu",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["mya"],
            "main_score": "f1",
        }