from ...abstasks.AbsTaskClassification import AbsTaskClassification


class VLSP2016Sentiment_vie_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "VLSP2016Sentiment_vie_Classification",
            "hf_hub_name": "kornwtp/vlsp2016sentiment-vie-classification",
            "description": "Sentiment analysis of personal opinions",
            "reference": "https://vlsp.org.vn/vlsp2016/eval/sa",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["vie"],
            "main_score": "f1",
        }