from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class VietnameseUITViCTSDClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "VietnameseUITViCTSDClassification",
            "hf_hub_name": "kornwtp/vi-uit-victsd-classification",
            "description": "The UIT-ViCTSD (Vietnamese Constructive and Toxic Speech Detection dataset) is a compilation of 10,000 human-annotated comments intended for constructive and toxic comments detection.",
            "reference": "https://github.com/tarudesu/ViCTSD",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["vi"],
            "main_score": "f1",
        }