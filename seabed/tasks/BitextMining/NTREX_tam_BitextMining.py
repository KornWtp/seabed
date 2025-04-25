from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class NTREX_tam_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "NTREX_tam_BitextMining",
            "hf_hub_name": "kornwtp/ntrex-tam-bitextmining",
            "description": "Parallel sentences in English and their corresponding sentences in Tamil.",
            "reference": "https://huggingface.co/datasets/mteb/NTREX",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["tamn"],
            "main_score": "f1",
        }