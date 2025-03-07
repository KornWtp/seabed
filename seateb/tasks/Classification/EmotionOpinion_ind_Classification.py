from ...abstasks.AbsTaskClassification import AbsTaskClassification


class EmotionOpinion_ind_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "EmotionOpinion_ind_Classification",
            "hf_hub_name": "kornwtp/emotion-opinion-ind-classification",
            "description": "Emotion ID Opinion is a dataset of Indonesian-language tweets conveying public opinion on a variety of topics.",
            "reference": "https://github.com/Ricco48/Emotion-Dataset-from-Indonesian-Public-Opinion",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["ind"],
            "main_score": "f1",
        }