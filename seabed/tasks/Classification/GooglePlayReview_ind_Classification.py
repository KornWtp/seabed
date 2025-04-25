from ...abstasks.AbsTaskClassification import AbsTaskClassification


class GooglePlayReview_ind_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "GooglePlayReview_ind_Classification",
            "hf_hub_name": "kornwtp/googleplay-review-ind-classification",
            "description": "Indonesian Google Play Review, dataset scrapped from e-commerce app on Google Play for sentiment analysis.",
            "reference": "https://github.com/jakartaresearch/hf-datasets/tree/main/google-play-review/google-play-review",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["ind"],
            "main_score": "f1",
        }