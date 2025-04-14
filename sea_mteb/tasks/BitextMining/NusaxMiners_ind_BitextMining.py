from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class NusaxMiners_ind_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "NusaxMiners_ind_BitextMining",
            "hf_hub_name": "kornwtp/nusax-miners-ind-bitextmining",
            "description": "Parallel sentences in English and their corresponding sentences in Indonesian.",
            "reference": "https://huggingface.co/datasets/gentaiscool/bitext_nusax_miners",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["ind"],
            "main_score": "f1",
        }