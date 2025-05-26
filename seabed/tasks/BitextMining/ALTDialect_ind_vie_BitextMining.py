from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class ALTDialect_ind_vie_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "ALTDialect_ind_vie_BitextMining",
            "hf_hub_name": "kornwtp/alt-ind-vie-bitextmining",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["vie"],
            "main_score": "f1",
        }