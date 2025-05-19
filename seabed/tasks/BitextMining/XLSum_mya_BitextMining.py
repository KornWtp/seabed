from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class XLSum_mya_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "XLSum_mya_BitextMining",
            "hf_hub_name": "kornwtp/xlsum-mya-bitextmining",
            "description": "",
            "reference": "https://github.com/csebuetnlp/xl-sum",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["mya"],
            "main_score": "f1",
        }