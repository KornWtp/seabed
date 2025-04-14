from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class NTREX_lao_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "NTREX_lao_BitextMining",
            "hf_hub_name": "kornwtp/ntrex-lao-bitextmining",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["lao"],
            "main_score": "f1",
        }