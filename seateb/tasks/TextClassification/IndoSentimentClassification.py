from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class IndoSentimentClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "IndoSentimentClassification",
            "hf_hub_name": "kornwtp/id-sentiment-classification",
            "description": "Sentiment classification from multilingual sentiment classification datasets.",
            "reference": "https://huggingface.co/datasets/mteb/multilingual-sentiment-classification",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "f1",
        }