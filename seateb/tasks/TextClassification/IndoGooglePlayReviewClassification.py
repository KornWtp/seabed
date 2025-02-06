from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class IndoGooglePlayReviewClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "IndoGooglePlayReviewClassification",
            "hf_hub_name": "kornwtp/id-google-play-review",
            "description": "Indonesian Google Play Review, dataset scrapped from e-commerce app on Google Play for sentiment analysis.",
            "reference": "https://github.com/jakartaresearch/hf-datasets/tree/main/google-play-review/google-play-review",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "f1",
        }