from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class XLSum_ind_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "XLSum_ind_BitextMining",
            "hf_hub_name": "kornwtp/xlsum-ind-bitextmining",
            "description": "",
            "reference": "https://github.com/csebuetnlp/xl-sum",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["ind"],
            "main_score": "f1",
        }