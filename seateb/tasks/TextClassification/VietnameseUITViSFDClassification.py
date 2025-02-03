from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class VietnameseUITViSFDClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "VietnameseUITViSFDClassification",
            "hf_hub_name": "kornwtp/vi-uit-visfd-classification",
            "description": "UIT-ViSFD is the Vietnamese Smartphone Feedback Dataset. It is an aspect-based sentiment analysis dataset.",
            "reference": "https://github.com/LuongPhan/UIT-ViSFD",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["vi"],
            "main_score": "f1",
        }