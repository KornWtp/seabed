from ...abstasks.AbsTaskPairClassification import AbsTaskPairClassification


class BurmeseXNLI(AbsTaskPairClassification):
    @property
    def description(self):
        return {
            "name": "BurmeseXNLI",
            "hf_hub_name": "kornwtp/my-xnli",
            "description": "Sentence pairs classification from the Cross-lingual Natural Language Inference (XNLI) corpus.",
            "reference": "https://huggingface.co/datasets/akhtet/myanmar-xnli",
            "category": "s2s",
            "type": "PairClassification",
            "eval_splits": ["test"],
            "eval_langs": ["my"],
            "main_score": "ap",
        }