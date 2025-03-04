from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class ThaiUSEmbassyBitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "ThaiUSEmbassyBitextMining",
            "hf_hub_name": "kornwtp/th-usembassy",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["th"],
            "main_score": "mean_accuracy",
        }