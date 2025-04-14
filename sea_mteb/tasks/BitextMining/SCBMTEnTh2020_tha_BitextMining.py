from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class SCBMTEnTh2020_tha_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "SCBMTEnTh2020_tha_BitextMining",
            "hf_hub_name": "kornwtp/scb-mt-enth2020-tha-bitextmining",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["tha"],
            "main_score": "f1",
        }