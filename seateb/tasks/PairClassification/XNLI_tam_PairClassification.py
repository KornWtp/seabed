from ...abstasks.AbsTaskPairClassification import AbsTaskPairClassification


class XNLI_tam_PairClassification(AbsTaskPairClassification):
    @property
    def description(self):
        return {
            "name": "XNLI_tam_PairClassification",
            "hf_hub_name": "kornwtp/xnli-tam-pairclassification",
            "description": "Sentence pairs classification similar to existing XNLI dataset in shape/form, but focusses on Indic language family.",
            "reference": "https://huggingface.co/datasets/Divyanshu/indicxnli",
            "category": "s2s",
            "type": "PairClassification",
            "eval_splits": ["test"],
            "eval_langs": ["tam"],
            "main_score": "ap",
        }