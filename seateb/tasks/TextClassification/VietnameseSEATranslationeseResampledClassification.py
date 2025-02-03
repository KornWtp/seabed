from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class VietnameseSEATranslationeseResampledClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "VietnameseSEATranslationeseResampledClassification",
            "hf_hub_name": "kornwtp/vietnamese-sea-translationese-resampled",
            "description": "Text classifier to discriminate between translationese and natural text in Vietnamese.",
            "reference": "https://huggingface.co/datasets/SEACrowd/sea_translationese_resampled",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["vi"],
            "main_score": "f1",
        }