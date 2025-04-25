from ...abstasks.AbsTaskClassification import AbsTaskClassification


class EMOT_ind_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "EMOT_ind_Classification",
            "hf_hub_name": "kornwtp/emot-ind-classification",
            "description": "An emotion classification dataset collected from the social media platform Twitter.",
            "reference": "https://huggingface.co/datasets/indonlp/indonlu",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["ind"],
            "main_score": "f1",
        }