from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class NTREX_fil_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "NTREX_fil_BitextMining",
            "hf_hub_name": "kornwtp/ntrex-fil-bitextmining",
            "description": "Parallel sentences in English and their corresponding sentences in Tagalog.",
            "reference": "https://huggingface.co/datasets/mteb/NTREX",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["fil"],
            "main_score": "f1",
        }