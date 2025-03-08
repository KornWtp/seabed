from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class ALT_mya_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "ALT_mya_BitextMining",
            "hf_hub_name": "kornwtp/alt-mya-bitextmining",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["mya"],
            "main_score": "f1",
        }