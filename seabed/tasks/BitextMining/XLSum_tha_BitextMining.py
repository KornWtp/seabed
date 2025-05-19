from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class XLSum_tha_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "XLSum_tha_BitextMining",
            "hf_hub_name": "kornwtp/xlsum-tha-bitextmining",
            "description": "",
            "reference": "https://github.com/csebuetnlp/xl-sum",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["tha"],
            "main_score": "f1",
        }