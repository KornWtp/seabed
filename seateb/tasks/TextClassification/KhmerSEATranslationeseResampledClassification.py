from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class KhmerSEATranslationeseResampledClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "KhmerSEATranslationeseResampledClassification",
            "hf_hub_name": "kornwtp/khmer-sea-translationese-resampled",
            "description": "Text classifier to discriminate between translationese and natural text in Khmer.",
            "reference": "https://huggingface.co/datasets/SEACrowd/sea_translationese_resampled",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["km"],
            "main_score": "f1",
        }