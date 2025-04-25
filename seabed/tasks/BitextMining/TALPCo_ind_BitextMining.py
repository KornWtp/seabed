from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class TALPCo_ind_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "TALPCo_ind_BitextMining",
            "hf_hub_name": "kornwtp/talpco-ind-bitextmining",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["ind"],
            "main_score": "f1",
        }