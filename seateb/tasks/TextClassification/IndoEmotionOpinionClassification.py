from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class IndoEmotionOpinionClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "IndoEmotionOpinionClassification",
            "hf_hub_name": "kornwtp/id-emotion-opinion-classification",
            "description": "Emotion ID Opinion is a dataset of Indonesian-language tweets conveying public opinion on a variety of topics.",
            "reference": "https://github.com/Ricco48/Emotion-Dataset-from-Indonesian-Public-Opinion",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "f1",
        }