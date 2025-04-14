from ...abstasks.AbsTaskClassification import AbsTaskClassification


class UITViSFD_vie_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "UITViSFD_vie_Classification",
            "hf_hub_name": "kornwtp/uitvisfd-vie-classification",
            "description": "UIT-ViSFD is the Vietnamese Smartphone Feedback Dataset. It is an aspect-based sentiment analysis dataset.",
            "reference": "https://github.com/LuongPhan/UIT-ViSFD",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["vie"],
            "main_score": "f1",
        }