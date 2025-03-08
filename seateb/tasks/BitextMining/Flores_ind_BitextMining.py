from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class Flores_ind_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "Flores_ind_BitextMining",
            "hf_hub_name": "kornwtp/flores-ind-bitextmining",
            "description": "Parallel sentences in English and their corresponding sentences in Indonesian.",
            "reference": "https://huggingface.co/datasets/mteb/flores",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["devtest"],
            "eval_langs": ["ind"],
            "main_score": "f1",
        }