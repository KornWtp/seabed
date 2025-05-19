from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class XLSum_vie_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "XLSum_vie_BitextMining",
            "hf_hub_name": "kornwtp/xlsum-vie-bitextmining",
            "description": "",
            "reference": "https://github.com/csebuetnlp/xl-sum",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["vie"],
            "main_score": "f1",
        }