from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class IndoSentimentAnalysisClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "IndoSentimentAnalysisClassification",
            "hf_hub_name": "kornwtp/id-sentiment-analysis-classification",
            "description": "This dataset consists of 10806 labeled Indonesian tweets with their corresponding sentiment analysis: positive, negative, and neutral, up to 2019.",
            "reference": "https://huggingface.co/datasets/SEACrowd/id_sentiment_analysis",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "f1",
        }