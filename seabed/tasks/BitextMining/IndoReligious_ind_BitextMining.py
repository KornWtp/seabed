from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class IndoReligious_ind_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "IndoReligious_ind_BitextMining",
            "hf_hub_name": "kornwtp/idreligious-ind-bitextmining",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["ind"],
            "main_score": "f1",
        }