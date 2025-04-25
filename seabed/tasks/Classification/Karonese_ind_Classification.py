from ...abstasks.AbsTaskClassification import AbsTaskClassification


class Karonese_ind_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "Karonese_ind_Classification",
            "hf_hub_name": "kornwtp/karonese-ind-classification",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["ind"],
            "main_score": "f1",
        }