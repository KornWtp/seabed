from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class IndoNLG_ind_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "IndoNLG_ind_BitextMining",
            "hf_hub_name": "kornwtp/indonlg-ind-bitextmining",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["ind"],
            "main_score": "f1",
        }