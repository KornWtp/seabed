from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class Flores_fil_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "Flores_fil_BitextMining",
            "hf_hub_name": "kornwtp/flores-fil-bitextmining",
            "description": "Parallel sentences in English and their corresponding sentences in Filipino.",
            "reference": "https://huggingface.co/datasets/mteb/flores",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["devtest"],
            "eval_langs": ["fil"],
            "main_score": "f1",
        }