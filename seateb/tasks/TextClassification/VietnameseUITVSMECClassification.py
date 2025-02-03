from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class VietnameseUITVSMECClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "VietnameseUITVSMECClassification",
            "hf_hub_name": "kornwtp/vi-uit-vsmec-classification",
            "description": "This dataset consists of Vietnamese Facebook comments that were manually annotated for sentiment.",
            "reference": "https://huggingface.co/datasets/SEACrowd/uit_vsmec",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["vi"],
            "main_score": "f1",
        }