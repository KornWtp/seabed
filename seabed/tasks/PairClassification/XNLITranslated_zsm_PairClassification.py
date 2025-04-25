from ...abstasks.AbsTaskPairClassification import AbsTaskPairClassification


class XNLI_zsm_PairClassification(AbsTaskPairClassification):
    @property
    def description(self):
        return {
            "name": "XNLI_zsm_PairClassification",
            "hf_hub_name": "kornwtp/xnli-zsm-pairclassification",
            "description": "Malay sentence pairs classification, translated from the Cross-lingual Natural Language Inference (XNLI) corpus using the Google Translate API.",
            "reference": "https://github.com/facebookresearch/XNLI",
            "category": "s2s",
            "type": "PairClassification",
            "eval_splits": ["test"],
            "eval_langs": ["zsm"],
            "main_score": "ap",
        }