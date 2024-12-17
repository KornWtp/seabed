from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class WongnaiReviews(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "WongnaiReviews",
            "hf_hub_name": "kornwtp/wongnai-reviews",
            "description": "The Wongnai Review dataset contains restaurant reviews and ratings, almost entirely in Thai language.",
            "reference": "https://huggingface.co/datasets/Wongnai/wongnai_reviews",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["th"],
            "main_score": "f1",
        }