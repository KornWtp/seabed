from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class Liputan6_ind_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "Liputan6_ind_BitextMining",
            "hf_hub_name": "kornwtp/liputan6-ind-bitextmining",
            "description": "",
            "reference": "https://github.com/fajri91/sum_liputan6",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["ind"],
            "main_score": "f1",
        }