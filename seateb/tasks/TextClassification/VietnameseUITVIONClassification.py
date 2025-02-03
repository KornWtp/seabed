from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class VietnameseUITVIONClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "VietnameseUITVIONClassification",
            "hf_hub_name": "kornwtp/vi-uit-vion-classification",
            "description": "UIT-ViON (Vietnamese Online Newspaper) is a dataset collected from well-known online newspapers in Vietnamese.",
            "reference": "https://github.com/kh4nh12/UIT-ViON-Dataset",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["vi"],
            "main_score": "f1",
        }