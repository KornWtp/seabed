from ...abstasks.AbsTaskClassification import AbsTaskClassification


class WisesightSentiment_tha_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "WisesightSentiment_tha_Classification",
            "hf_hub_name": "kornwtp/wisesight-sentiment-tha-classification",
            "description": "Social media messages in Thai language with sentiment label (positive, neutral, negative, question)",
            "reference": "https://huggingface.co/datasets/pythainlp/wisesight_sentiment",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["tha"],
            "main_score": "f1",
        }