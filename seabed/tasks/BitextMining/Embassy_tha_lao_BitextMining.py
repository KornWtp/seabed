from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class Embassy_tha_lao_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "Embassy_tha_lao_BitextMining",
            "hf_hub_name": "kornwtp/embassy-tha-lao-bitextmining",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["tha"],
            "main_score": "f1",
        }