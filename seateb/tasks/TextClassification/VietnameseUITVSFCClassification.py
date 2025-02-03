from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class VietnameseUITVSFCClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "VietnameseUITVSFCClassification",
            "hf_hub_name": "kornwtp/vi-uit-vsfc-classification",
            "description": "This corpus consists of student feedback obtained from end-of-semester surveys at a Vietnamese university.",
            "reference": "https://huggingface.co/datasets/SEACrowd/uit_vsfc",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["vi"],
            "main_score": "f1",
        }