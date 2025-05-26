from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class ALTDialect_vie_khm_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "ALTDialect_vie_khm_BitextMining",
            "hf_hub_name": "kornwtp/alt-vie-khm-bitextmining",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["khm"],
            "main_score": "f1",
        }