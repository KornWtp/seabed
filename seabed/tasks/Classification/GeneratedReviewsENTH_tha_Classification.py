from ...abstasks.AbsTaskClassification import AbsTaskClassification


class GeneratedReviewsENTH_tha_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "GeneratedReviewsENTH_tha_Classification",
            "hf_hub_name": "kornwtp/generated-reviews-enth-tha-classification",
            "description": "English-to-Thai translation quality estimation (binary label)",
            "reference": "https://huggingface.co/datasets/airesearch/generated_reviews_enth",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["tha"],
            "main_score": "f1",
        }