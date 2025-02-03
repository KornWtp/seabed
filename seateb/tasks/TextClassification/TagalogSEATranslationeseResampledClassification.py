from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class TagalogSEATranslationeseResampledClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "TagalogSEATranslationeseResampledClassification",
            "hf_hub_name": "kornwtp/tagalog-sea-translationese-resampled",
            "description": "Text classifier to discriminate between translationese and natural text in tagalog or filipino.",
            "reference": "https://huggingface.co/datasets/SEACrowd/sea_translationese_resampled",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["tl"],
            "main_score": "f1",
        }