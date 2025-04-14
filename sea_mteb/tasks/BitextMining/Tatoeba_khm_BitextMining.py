from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class Tatoeba_khm_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "Tatoeba_khm_BitextMining",
            "hf_hub_name": "kornwtp/tatoeba-khm-bitextmining",
            "description": "Parallel sentences in English and their corresponding sentences in Khmer.",
            "reference": "https://opus.nlpl.eu",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["khm"],
            "main_score": "f1",
        }