from ...abstasks.AbsTaskPairClassification import AbsTaskPairClassification


class XNLI_khm_PairClassification(AbsTaskPairClassification):
    @property
    def description(self):
        return {
            "name": "XNLI_khm_PairClassification",
            "hf_hub_name": "kornwtp/xnli-khm-pairclassification",
            "description": "Khmer sentence pairs classification, translated from the Cross-lingual Natural Language Inference (XNLI) corpus using the Google Translate API.",
            "reference": "https://github.com/facebookresearch/XNLI",
            "category": "s2s",
            "type": "PairClassification",
            "eval_splits": ["test"],
            "eval_langs": ["khm"],
            "main_score": "ap",
        }