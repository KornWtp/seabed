from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class NTREX_ind_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "NTREX_ind_BitextMining",
            "hf_hub_name": "kornwtp/ntrex-ind-bitextmining",
            "description": "Parallel sentences in English and their corresponding sentences in Indonesian.",
            "reference": "https://huggingface.co/datasets/mteb/NTREX",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["ind"],
            "main_score": "f1",
        }