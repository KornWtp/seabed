from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class BurmeseSIB200Classification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "BurmeseSIB200Classification",
            "hf_hub_name": "kornwtp/my-sib_200",
            "description": "SIB-200 is the largest publicly available topic classification dataset based on Flores-200 covering 205 languages and dialects.",
            "reference": "https://github.com/dadelani/sib-200",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["my"],
            "main_score": "f1",
        }