from ...abstasks.AbsTaskPairClassification import AbsTaskPairClassification


class MalayXNLI(AbsTaskPairClassification):
    @property
    def description(self):
        return {
            "name": "MalayXNLIPairClassification",
            "hf_hub_name": "kornwtp/ms-xnli",
            "description": "Malay sentence pairs classification, translated from the Cross-lingual Natural Language Inference (XNLI) corpus using the Google Translate API.",
            "reference": "https://github.com/facebookresearch/XNLI",
            "category": "s2s",
            "type": "PairClassification",
            "eval_splits": ["test"],
            "eval_langs": ["ms"],
            "main_score": "ap",
        }