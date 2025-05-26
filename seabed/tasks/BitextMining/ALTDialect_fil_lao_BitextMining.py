from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class ALTDialect_fil_lao_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "ALTDialect_fil_lao_BitextMining",
            "hf_hub_name": "kornwtp/alt-fil-lao-bitextmining",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["lao"],
            "main_score": "f1",
        }