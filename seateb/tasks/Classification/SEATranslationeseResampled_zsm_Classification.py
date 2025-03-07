from ...abstasks.AbsTaskClassification import AbsTaskClassification


class SEATranslationeseResampled_zsm_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "SEATranslationeseResampled_zsm_Classification",
            "hf_hub_name": "kornwtp/sea-translationese-resampled-zsm-classification",
            "description": "Text classifier to discriminate between translationese and natural text in malay.",
            "reference": "https://huggingface.co/datasets/SEACrowd/sea_translationese_resampled",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["zsm"],
            "main_score": "f1",
        }