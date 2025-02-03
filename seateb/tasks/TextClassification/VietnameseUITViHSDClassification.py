from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class VietnameseUITViHSDClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "VietnameseUITViHSDClassification",
            "hf_hub_name": "kornwtp/vi-uit-vihsd-classification",
            "description": "The ViHSD dataset consists of comments collected from Facebook pages and YouTube channels that have a high-interactive rate, and do not restrict comments.",
            "reference": "https://github.com/sonlam1102/vihsd",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["vi"],
            "main_score": "f1",
        }