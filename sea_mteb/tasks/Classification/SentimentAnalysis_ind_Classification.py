from ...abstasks.AbsTaskClassification import AbsTaskClassification


class SentimentAnalysis_ind_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "SentimentAnalysis_ind_Classification",
            "hf_hub_name": "kornwtp/sentiment-analysis-ind-classification",
            "description": "This dataset consists of 10806 labeled Indonesian tweets with their corresponding sentiment analysis: positive, negative, and neutral, up to 2019.",
            "reference": "https://huggingface.co/datasets/SEACrowd/id_sentiment_analysis",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["ind"],
            "main_score": "f1",
        }