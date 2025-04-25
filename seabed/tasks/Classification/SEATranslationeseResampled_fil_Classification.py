from ...abstasks.AbsTaskClassification import AbsTaskClassification


class SEATranslationeseResampled_fil_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "SEATranslationeseResampled_fil_Classification",
            "hf_hub_name": "kornwtp/sea-translationese-resampled-fil-classification",
            "description": "Text classifier to discriminate between translationese and natural text in tagalog or filipino.",
            "reference": "https://huggingface.co/datasets/SEACrowd/sea_translationese_resampled",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["fil"],
            "main_score": "f1",
        }