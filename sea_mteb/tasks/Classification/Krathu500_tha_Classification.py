from ...abstasks.AbsTaskClassification import AbsTaskClassification


class Krathu500_tha_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "Krathu500_tha_Classification",
            "hf_hub_name": "kornwtp/krathu500-tha-classification",
            "description": "Thai text classification from post-comment on Pantip, a popular Thai web board.",
            "reference": "https://github.com/Pittawat2542/krathu-500",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["tha"],
            "main_score": "f1",
        }