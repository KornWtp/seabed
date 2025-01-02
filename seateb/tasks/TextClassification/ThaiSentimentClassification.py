from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class ThaiSentimentClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "ThaiSentimentClassification",
            "hf_hub_name": "kornwtp/th-sentiment-classification",
            "description": "Sentiment classification from multilingual sentiment classification datasets.",
            "reference": "https://huggingface.co/datasets/mteb/multilingual-sentiment-classification",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["th"],
            "main_score": "f1",
        }