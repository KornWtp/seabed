from ...abstasks.AbsTaskPairClassification import AbsTaskPairClassification


class PAWS_fil_PairClassification(AbsTaskPairClassification):
    @property
    def description(self):
        return {
            "name": "PAWS_fil_PairClassification",
            "hf_hub_name": "kornwtp/paws-fil-pairclassificatioin",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "PairClassification",
            "eval_splits": ["train"],
            "eval_langs": ["fil"],
            "main_score": "ap",
        }