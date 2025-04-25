from ...abstasks.AbsTaskClassification import AbsTaskClassification


class SEATranslationeseResampled_tha_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "SEATranslationeseResampled_tha_Classification",
            "hf_hub_name": "kornwtp/sea-translationese-resampled-tha-classification",
            "description": "Text classifier to discriminate between translationese and natural text in Thai.",
            "reference": "https://huggingface.co/datasets/SEACrowd/sea_translationese_resampled",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["tha"],
            "main_score": "f1",
        }