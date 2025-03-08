from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class TALPCo_mya_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "TALPCo_mya_BitextMining",
            "hf_hub_name": "kornwtp/talpco-mya-bitextmining",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["mya"],
            "main_score": "f1",
        }