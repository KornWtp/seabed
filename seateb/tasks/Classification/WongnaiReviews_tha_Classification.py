from ...abstasks.AbsTaskClassification import AbsTaskClassification


class WongnaiReviews_tha_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "WongnaiReviews_tha_Classification",
            "hf_hub_name": "kornwtp/wongnai-reviews-tha-classification",
            "description": "The Wongnai Review dataset contains restaurant reviews and ratings, almost entirely in Thai language.",
            "reference": "https://huggingface.co/datasets/Wongnai/wongnai_reviews",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["tha"],
            "main_score": "f1",
        }