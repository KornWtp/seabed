from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class VSoLSCSum_vie_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "VSoLSCSum_vie_BitextMining",
            "hf_hub_name": "kornwtp/vsolscsum-vie-bitextmining",
            "description": "",
            "reference": "https://github.com/nguyenlab/VSoLSCSum-Dataset",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["vie"],
            "main_score": "f1",
        }