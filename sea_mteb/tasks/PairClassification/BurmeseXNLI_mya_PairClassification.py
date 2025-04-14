from ...abstasks.AbsTaskPairClassification import AbsTaskPairClassification


class BurmeseXNLI_mya_PairClassification(AbsTaskPairClassification):
    @property
    def description(self):
        return {
            "name": "BurmeseXNLI_mya_PairClassification",
            "hf_hub_name": "kornwtp/burmese-xnli-mya-pairclassification",
            "description": "Sentence pairs classification from the Cross-lingual Natural Language Inference (XNLI) corpus.",
            "reference": "https://huggingface.co/datasets/akhtet/myanmar-xnli",
            "category": "s2s",
            "type": "PairClassification",
            "eval_splits": ["test"],
            "eval_langs": ["mya"],
            "main_score": "ap",
        }