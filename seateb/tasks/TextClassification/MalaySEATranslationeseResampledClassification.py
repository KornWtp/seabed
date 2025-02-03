from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class MalaySEATranslationeseResampledClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "MalaySEATranslationeseResampledClassification",
            "hf_hub_name": "kornwtp/malay-sea-translationese-resampled",
            "description": "Text classifier to discriminate between translationese and natural text in malay.",
            "reference": "https://huggingface.co/datasets/SEACrowd/sea_translationese_resampled",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["ms"],
            "main_score": "f1",
        }