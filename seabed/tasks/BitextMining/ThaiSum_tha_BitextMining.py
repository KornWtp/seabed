from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class ThaiSum_tha_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "ThaiSum_tha_BitextMining",
            "hf_hub_name": "kornwtp/thaisum-tha-bitextmining",
            "description": "",
            "reference": "https://github.com/nakhunchumpolsathien/ThaiSum",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["tha"],
            "main_score": "f1",
        }