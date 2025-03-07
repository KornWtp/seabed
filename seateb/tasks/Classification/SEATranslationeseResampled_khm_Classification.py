from ...abstasks.AbsTaskClassification import AbsTaskClassification


class SEATranslationeseResampled_khm_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "SEATranslationeseResampled_khm_Classification",
            "hf_hub_name": "kornwtp/sea-translationese-resampled-khm-classification",
            "description": "Text classifier to discriminate between translationese and natural text in Khmer.",
            "reference": "https://huggingface.co/datasets/SEACrowd/sea_translationese_resampled",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["khm"],
            "main_score": "f1",
        }