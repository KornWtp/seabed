from ...abstasks.AbsTaskPairClassification import AbsTaskPairClassification


class ThaiXNLI(AbsTaskPairClassification):
    @property
    def description(self):
        return {
            "name": "ThaiXNLIPairClassification",
            "hf_hub_name": "kornwtp/th-xnli",
            "description": "Sentence pairs classification from the Cross-lingual Natural Language Inference (XNLI) corpus.",
            "reference": "https://github.com/facebookresearch/XNLI",
            "category": "s2s",
            "type": "PairClassification",
            "eval_splits": ["test"],
            "eval_langs": ["th"],
            "main_score": "ap",
        }