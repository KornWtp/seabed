from ...abstasks.AbsTaskPairClassification import AbsTaskPairClassification


class TamilXNLI(AbsTaskPairClassification):
    @property
    def description(self):
        return {
            "name": "TamilXNLIPairClassification",
            "hf_hub_name": "kornwtp/ta-xnli",
            "description": "Sentence pairs classification similar to existing XNLI dataset in shape/form, but focusses on Indic language family.",
            "reference": "https://huggingface.co/datasets/Divyanshu/indicxnli",
            "category": "s2s",
            "type": "PairClassification",
            "eval_splits": ["test"],
            "eval_langs": ["ta"],
            "main_score": "ap",
        }