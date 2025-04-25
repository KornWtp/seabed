from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class Flores_tam_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "Flores_tam_BitextMining",
            "hf_hub_name": "kornwtp/flores-tam-bitextmining",
            "description": "Parallel sentences in English and their corresponding sentences in Tamil.",
            "reference": "https://huggingface.co/datasets/mteb/flores",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["devtest"],
            "eval_langs": ["tam"],
            "main_score": "f1",
        }