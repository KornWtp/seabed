from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class Flores_lao_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "Flores_lao_BitextMining",
            "hf_hub_name": "kornwtp/flores-lao-bitextmining",
            "description": "Parallel sentences in English and their corresponding sentences in Lao.",
            "reference": "https://huggingface.co/datasets/mteb/flores",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["devtest"],
            "eval_langs": ["lao"],
            "main_score": "f1",
        }