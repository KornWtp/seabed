from ...abstasks.AbsTaskPairClassification import AbsTaskPairClassification


class IndoWReTE(AbsTaskPairClassification):
    @property
    def description(self):
        return {
            "name": "IndoWReTEPairClassification",
            "hf_hub_name": "kornwtp/id-wrete",
            "description": "Sentence pairs classification from Wiki Revision Edits Textual Entailment dataset.",
            "reference": "https://huggingface.co/datasets/indonlp/indonlu",
            "category": "s2s",
            "type": "PairClassification",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "ap",
        }