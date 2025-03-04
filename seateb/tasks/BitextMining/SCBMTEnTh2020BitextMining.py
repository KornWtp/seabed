from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class SCBMTEnTh2020BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "SCBMTEnTh2020BitextMining",
            "hf_hub_name": "kornwtp/scb-mt-en-th-2020",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["th"],
            "main_score": "mean_accuracy",
        }