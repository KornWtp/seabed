from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class LaoNTREXBitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "LaoNTREXBitextMining",
            "hf_hub_name": "kornwtp/lo-ntrex",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["lo"],
            "main_score": "f1",
        }