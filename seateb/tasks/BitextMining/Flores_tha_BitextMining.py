from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class Flores_tha_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "Flores_tha_BitextMining",
            "hf_hub_name": "kornwtp/flores-tha-bitextmining",
            "description": "Parallel sentences in English and their corresponding sentences in Thai.",
            "reference": "https://huggingface.co/datasets/mteb/flores",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["devtest"],
            "eval_langs": ["tha"],
            "main_score": "f1",
        }