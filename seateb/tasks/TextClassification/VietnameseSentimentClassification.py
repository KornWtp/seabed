from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class VietnameseSentimentClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "VietnameseSentimentClassification",
            "hf_hub_name": "kornwtp/vi-sentiment-classification",
            "description": "Sentiment classification from multilingual sentiment classification datasets.",
            "reference": "https://huggingface.co/datasets/mteb/multilingual-sentiment-classification",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["vi"],
            "main_score": "f1",
        }