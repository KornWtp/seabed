from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class BurmeseSEATranslationeseResampledClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "BurmeseSEATranslationeseResampledClassification",
            "hf_hub_name": "kornwtp/Khine-myanmar-news-classification",
            "description": "Text classifier to discriminate between translationese and natural text in Burmese.",
            "reference": "https://huggingface.co/datasets/SEACrowd/sea_translationese_resampled",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["my"],
            "main_score": "f1",
        }