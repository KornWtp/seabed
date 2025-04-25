from ...abstasks.AbsTaskClassification import AbsTaskClassification


class SEATranslationeseResampled_vie_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "SEATranslationeseResampled_vie_Classification",
            "hf_hub_name": "kornwtp/sea-translationese-resampled-vie-classification",
            "description": "Text classifier to discriminate between translationese and natural text in Vietnamese.",
            "reference": "https://huggingface.co/datasets/SEACrowd/sea_translationese_resampled",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["vie"],
            "main_score": "f1",
        }