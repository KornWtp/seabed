from ...abstasks.AbsTaskClassification import AbsTaskClassification


class SEATranslationeseResampled_ind_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "SEATranslationeseResampled_ind_Classification",
            "hf_hub_name": "kornwtp/sea-translationese-resampled-ind-classificaiton",
            "description": "Text classifier to discriminate between translationese and natural text in Indonesian.",
            "reference": "https://huggingface.co/datasets/SEACrowd/sea_translationese_resampled",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["ind"],
            "main_score": "f1",
        }