from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class ALT_khm_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "ALT_khm_BitextMining",
            "hf_hub_name": "kornwtp/alt-khm-bitextmining",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["khm"],
            "main_score": "f1",
        }