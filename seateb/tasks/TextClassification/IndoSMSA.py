from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class IndoSMSA(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "IndoSMSA",
            "hf_hub_name": "kornwtp/indonlu-smsa",
            "description": "A sentence-level sentiment analysis dataset consisting of comments and reviews in Indonesian, collected from multiple online platforms.",
            "reference": "https://huggingface.co/datasets/indonlp/indonlu",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "f1",
        }