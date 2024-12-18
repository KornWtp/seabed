from ...abstasks.AbsTaskPairClassification import AbsTaskPairClassification


class TamilXNLI(AbsTaskPairClassification):
    @property
    def description(self):
        return {
            "name": "TamilXNLI",
            "hf_hub_name": "kornwtp/tl-xnli",
            "description": "Sentence pairs classification from the Cross-lingual Natural Language Inference (XNLI) corpus.",
            "reference": "https://github.com/facebookresearch/XNLI",
            "category": "s2s",
            "type": "PairClassification",
            "eval_splits": ["validation", "test"],
            "eval_langs": ["ta"],
            "main_score": "ap",
        }