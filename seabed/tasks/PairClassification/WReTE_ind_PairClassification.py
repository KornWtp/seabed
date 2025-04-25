from ...abstasks.AbsTaskPairClassification import AbsTaskPairClassification


class WReTE_ind_PairClassification(AbsTaskPairClassification):
    @property
    def description(self):
        return {
            "name": "WReTE_ind_PairClassification",
            "hf_hub_name": "kornwtp/wrete-ind-pairclassification",
            "description": "Sentence pairs classification from Wiki Revision Edits Textual Entailment dataset.",
            "reference": "https://huggingface.co/datasets/indonlp/indonlu",
            "category": "s2s",
            "type": "PairClassification",
            "eval_splits": ["test"],
            "eval_langs": ["ind"],
            "main_score": "ap",
        }