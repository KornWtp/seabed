from ...abstasks.AbsTaskPairClassification import AbsTaskPairClassification


class IndoNLI(AbsTaskPairClassification):
    @property
    def description(self):
        return {
            "name": "IndoNLIPairClassification",
            "hf_hub_name": "kornwtp/id-nli",
            "description": "Sentence pairs classification from the Natural Language Inference (NLI) dataset for Indonesian corpus.",
            "reference": "https://huggingface.co/datasets/afaji/indonli",
            "category": "s2s",
            "type": "PairClassification",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "ap",
        }