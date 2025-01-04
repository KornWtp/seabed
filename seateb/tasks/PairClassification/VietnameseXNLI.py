from ...abstasks.AbsTaskPairClassification import AbsTaskPairClassification


class VietnameseXNLI(AbsTaskPairClassification):
    @property
    def description(self):
        return {
            "name": "VietnameseXNLI",
            "hf_hub_name": "kornwtp/vi-xnli",
            "description": "Sentence pairs classification from the Cross-lingual Natural Language Inference (XNLI) corpus.",
            "reference": "https://github.com/facebookresearch/XNLI",
            "category": "s2s",
            "type": "PairClassification",
            "eval_splits": ["validation", "test"],
            "eval_langs": ["vi"],
            "main_score": "ap",
        }