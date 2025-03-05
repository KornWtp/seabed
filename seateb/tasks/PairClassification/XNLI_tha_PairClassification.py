from ...abstasks.AbsTaskPairClassification import AbsTaskPairClassification


class XNLI_tha_PairClassification(AbsTaskPairClassification):
    @property
    def description(self):
        return {
            "name": "XNLI_tha_PairClassification",
            "hf_hub_name": "kornwtp/xnli-tha-pairclassification",
            "description": "Sentence pairs classification from the Cross-lingual Natural Language Inference (XNLI) corpus.",
            "reference": "https://github.com/facebookresearch/XNLI",
            "category": "s2s",
            "type": "PairClassification",
            "eval_splits": ["test"],
            "eval_langs": ["tha"],
            "main_score": "ap",
        }