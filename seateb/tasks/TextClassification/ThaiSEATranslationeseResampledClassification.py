from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class ThaiSEATranslationeseResampledClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "ThaiSEATranslationeseResampledClassification",
            "hf_hub_name": "kornwtp/thai-sea-translationese-resampled",
            "description": "Text classifier to discriminate between translationese and natural text in Thai.",
            "reference": "https://huggingface.co/datasets/SEACrowd/sea_translationese_resampled",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["th"],
            "main_score": "f1",
        }