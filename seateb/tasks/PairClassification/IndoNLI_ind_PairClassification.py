from ...abstasks.AbsTaskPairClassification import AbsTaskPairClassification


class IndoNLI_ind_PairClassification(AbsTaskPairClassification):
    @property
    def description(self):
        return {
            "name": "IndoNLI_ind_PairClassification",
            "hf_hub_name": "kornwtp/idnli-ind-pairclassification",
            "description": "Sentence pairs classification from the Natural Language Inference (NLI) dataset for Indonesian corpus.",
            "reference": "https://huggingface.co/datasets/afaji/indonli",
            "category": "s2s",
            "type": "PairClassification",
            "eval_splits": ["test"],
            "eval_langs": ["ind"],
            "main_score": "ap",
        }