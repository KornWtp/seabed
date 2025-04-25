from ...abstasks.AbsTaskClassification import AbsTaskClassification


class SIB200_ind_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "SIB200_ind_Classification",
            "hf_hub_name": "kornwtp/sib200-ind-classification",
            "description": "SIB-200 is the largest publicly available topic classification dataset based on Flores-200 covering 205 languages and dialects.",
            "reference": "https://github.com/dadelani/sib-200",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["ind"],
            "main_score": "f1",
        }