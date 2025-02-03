from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class ThaiKrathu500Classification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "ThaiKrathu500Classification",
            "hf_hub_name": "kornwtp/krathu-500-classification",
            "description": "Thai text classification from post-comment on Pantip, a popular Thai web board.",
            "reference": "https://github.com/Pittawat2542/krathu-500",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["th"],
            "main_score": "f1",
        }