from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class ThaiGov_tha_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "ThaiGov_tha_BitextMining",
            "hf_hub_name": "kornwtp/thaigov-tha-bitextmining",
            "description": "",
            "reference": "https://github.com/PyThaiNLP/thaigov-v2-corpus",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["tha"],
            "main_score": "f1",
        }