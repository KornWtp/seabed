from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class MADLAD400_tet_Classification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "MADLAD400_tet_Classification",
            "hf_hub_name": "kornwtp/madlad400-tet-classification",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["tet"],
            "main_score": "f1",
        }