from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class ALTDialect_ind_tha_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "ALTDialect_ind_tha_BitextMining",
            "hf_hub_name": "kornwtp/alt-ind-tha-bitextmining",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["tha"],
            "main_score": "f1",
        }