from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class NTREX_khm_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "NTREX_khm_BitextMining",
            "hf_hub_name": "kornwtp/ntrex-khm-bitextmining",
            "description": "Parallel sentences in English and their corresponding sentences in Khmer.",
            "reference": "https://huggingface.co/datasets/mteb/IN22-Conv",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["khm"],
            "main_score": "f1",
        }