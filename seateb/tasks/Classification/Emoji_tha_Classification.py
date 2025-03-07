from ...abstasks.AbsTaskClassification import AbsTaskClassification


class Emoji_tha_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "Emoji_tha_Classification",
            "hf_hub_name": "kornwtp/emoji-tha-classification",
            "description": "Emojification of Thai Text",
            "reference": "https://github.com/kobkrit/thai-emojification",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["tha"],
            "main_score": "f1",
        }