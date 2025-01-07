from ...abstasks.AbsTaskPairClassification import AbsTaskPairClassification


class KhmerXNLI(AbsTaskPairClassification):
    @property
    def description(self):
        return {
            "name": "KhmerXNLIPairClassification",
            "hf_hub_name": "kornwtp/km-xnli",
            "description": "Khmer sentence pairs classification, translated from the Cross-lingual Natural Language Inference (XNLI) corpus using the Google Translate API.",
            "reference": "https://github.com/facebookresearch/XNLI",
            "category": "s2s",
            "type": "PairClassification",
            "eval_splits": ["test"],
            "eval_langs": ["km"],
            "main_score": "ap",
        }