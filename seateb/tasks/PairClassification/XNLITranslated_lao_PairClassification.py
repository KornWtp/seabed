from ...abstasks.AbsTaskPairClassification import AbsTaskPairClassification


class XNLI_lao_PairClassification(AbsTaskPairClassification):
    @property
    def description(self):
        return {
            "name": "XNLI_lao_PairClassification",
            "hf_hub_name": "kornwtp/xnli-lao-pairclassification",
            "description": "Sentence pairs classification from the Cross-lingual Natural Language Inference (XNLI) corpus.",
            "reference": "https://github.com/facebookresearch/XNLI",
            "category": "s2s",
            "type": "PairClassification",
            "eval_splits": ["test"],
            "eval_langs": ["lao"],
            "main_score": "ap",
        }