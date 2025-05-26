from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class ALTDialect_vie_fil_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "ALTDialect_vie_fil_BitextMining",
            "hf_hub_name": "kornwtp/alt-vie-fil-bitextmining",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["fil"],
            "main_score": "f1",
        }