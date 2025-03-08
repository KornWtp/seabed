from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class ALT_fil_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "ALT_fil_BitextMining",
            "hf_hub_name": "kornwtp/alt-fil-bitextmining",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["fil"],
            "main_score": "f1",
        }