from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class SoftwareDocumentation_ind_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "SoftwareDocumentation_ind_BitextMining",
            "hf_hub_name": "kornwtp/software-documentation-ind-bitextmining",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["ind"],
            "main_score": "f1",
        }