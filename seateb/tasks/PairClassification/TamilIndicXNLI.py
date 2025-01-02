from ...abstasks.AbsTaskPairClassification import AbsTaskPairClassification


class TamilIndicXNLI(AbsTaskPairClassification):
    @property
    def description(self):
        return {
            "name": "TamilIndicXNLI",
            "hf_hub_name": "kornwtp/ta-indicxnli",
            "description": "Sentence pairs classification similar to existing XNLI dataset in shape/form, but focusses on Indic language family.",
            "reference": "https://huggingface.co/datasets/Divyanshu/indicxnli",
            "category": "s2s",
            "type": "PairClassification",
            "eval_splits": ["validation", "test"],
            "eval_langs": ["ta"],
            "main_score": "ap",
        }