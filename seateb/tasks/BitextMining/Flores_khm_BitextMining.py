from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class Flores_khm_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "Flores_khm_BitextMining",
            "hf_hub_name": "kornwtp/flores-khm-bitextmining",
            "description": "Parallel sentences in English and their corresponding sentences in Khmer.",
            "reference": "https://huggingface.co/datasets/mteb/flores",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["devtest"],
            "eval_langs": ["khm"],
            "main_score": "f1",
        }