from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class SoftwareDocumentation_vie_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "SoftwareDocumentation_vie_BitextMining",
            "hf_hub_name": "kornwtp/software-documentation-vie-bitextmining",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["vie"],
            "main_score": "f1",
        }