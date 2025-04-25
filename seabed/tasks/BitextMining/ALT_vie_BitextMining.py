from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class ALT_vie_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "ALT_vie_BitextMining",
            "hf_hub_name": "kornwtp/alt-vie-bitextmining",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["vie"],
            "main_score": "f1",
        }