from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class IndoSEATranslationeseResampledClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "IndoSEATranslationeseResampledClassification",
            "hf_hub_name": "kornwtp/indo-sea-translationese-resampled",
            "description": "Text classifier to discriminate between translationese and natural text in Indonesian.",
            "reference": "https://huggingface.co/datasets/SEACrowd/sea_translationese_resampled",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "f1",
        }