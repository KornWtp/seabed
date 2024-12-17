from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class IndoEMOT(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "IndoEMOT",
            "hf_hub_name": "kornwtp/indonlu-emot",
            "description": "An emotion classification dataset collected from the social media platform Twitter.",
            "reference": "https://huggingface.co/datasets/indonlp/indonlu",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "f1",
        }