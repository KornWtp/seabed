from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class ThaiEmojiClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "ThaiEmojiClassification",
            "hf_hub_name": "kornwtp/th-emoji-classification",
            "description": "Emojification of Thai Text",
            "reference": "https://github.com/kobkrit/thai-emojification",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["th"],
            "main_score": "f1",
        }