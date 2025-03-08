from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class TALPCo_vie_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "TALPCo_vie_BitextMining",
            "hf_hub_name": "kornwtp/talpco-vie-bitextmining",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["vie"],
            "main_score": "f1",
        }