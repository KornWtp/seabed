from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class Flores_mya_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "Flores_mya_BitextMining",
            "hf_hub_name": "kornwtp/flores-mya-bitextmining",
            "description": "Parallel sentences in English and their corresponding sentences in Burmese.",
            "reference": "https://huggingface.co/datasets/mteb/flores",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["devtest"],
            "eval_langs": ["mya"],
            "main_score": "f1",
        }