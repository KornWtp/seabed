from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class GeneratedReviewsENTH(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "GeneratedReviewsENTHTextClassification",
            "hf_hub_name": "kornwtp/generated-reviews-enth",
            "description": "English-to-Thai translation quality estimation (binary label)",
            "reference": "https://huggingface.co/datasets/airesearch/generated_reviews_enth",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["th"],
            "main_score": "f1",
        }