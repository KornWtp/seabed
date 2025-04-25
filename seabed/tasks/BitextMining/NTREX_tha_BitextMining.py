from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class NTREX_tha_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "NTREX_tha_BitextMining",
            "hf_hub_name": "kornwtp/ntrex-tha-bitextmining",
            "description": "Parallel sentences in English and their corresponding sentences in Thai.",
            "reference": "https://huggingface.co/datasets/mteb/NTREX",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["tha"],
            "main_score": "f1",
        }