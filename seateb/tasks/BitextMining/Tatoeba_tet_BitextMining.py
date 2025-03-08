from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class Tatoeba_tet_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "Tatoeba_tet_BitextMining",
            "hf_hub_name": "kornwtp/tatoeba-tet-bitextmining",
            "description": "Parallel sentences in English and their corresponding sentences in Tetum.",
            "reference": "https://opus.nlpl.eu",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["tet"],
            "main_score": "f1",
        }