from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class ALTDialect_tha_khm_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "ALTDialect_tha_khm_BitextMining",
            "hf_hub_name": "kornwtp/alt-tha-khm-bitextmining",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["khm"],
            "main_score": "f1",
        }