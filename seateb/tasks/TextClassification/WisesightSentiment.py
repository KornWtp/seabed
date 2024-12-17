from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class WisesightSentiment(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "WisesightSentiment",
            "hf_hub_name": "kornwtp/wisesight-sentiment",
            "description": "Social media messages in Thai language with sentiment label (positive, neutral, negative, question)",
            "reference": "https://huggingface.co/datasets/pythainlp/wisesight_sentiment",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["th"],
            "main_score": "f1",
        }