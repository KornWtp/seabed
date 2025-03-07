from ...abstasks.AbsTaskPairClassification import AbsTaskPairClassification


class XNLI_vie_PairClassification(AbsTaskPairClassification):
    @property
    def description(self):
        return {
            "name": "XNLI_vie_PairClassification",
            "hf_hub_name": "kornwtp/xnli-vie-pairclassification",
            "description": "Sentence pairs classification from the Cross-lingual Natural Language Inference (XNLI) corpus.",
            "reference": "https://github.com/facebookresearch/XNLI",
            "category": "s2s",
            "type": "PairClassification",
            "eval_splits": ["test"],
            "eval_langs": ["vie"],
            "main_score": "ap",
        }