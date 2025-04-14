from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class SoftwareDocumentation_zsm_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "SoftwareDocumentation_zsm_BitextMining",
            "hf_hub_name": "kornwtp/software-documentation-zsm-bitextmining",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["zsm"],
            "main_score": "f1",
        }