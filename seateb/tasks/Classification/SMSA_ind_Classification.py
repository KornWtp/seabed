from ...abstasks.AbsTaskClassification import AbsTaskClassification


class SMSA_ind_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "SMSA_ind_Classification",
            "hf_hub_name": "kornwtp/smsa-ind-classification",
            "description": "A sentence-level sentiment analysis dataset consisting of comments and reviews in Indonesian, collected from multiple online platforms.",
            "reference": "https://huggingface.co/datasets/indonlp/indonlu",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["ind"],
            "main_score": "f1",
        }