from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class NTREX_mya_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "NTREX_mya_BitextMining",
            "hf_hub_name": "kornwtp/ntrex-mya-bitextmining",
            "description": "Parallel sentences in English and their corresponding sentences in Burmese.",
            "reference": "https://huggingface.co/datasets/mteb/NTREX",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["mya"],
            "main_score": "f1",
        }