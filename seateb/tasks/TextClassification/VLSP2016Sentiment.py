from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class VLSP2016Sentiment(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "VLSP2016Sentiment",
            "hf_hub_name": "kornwtp/vlsp2016",
            "description": "Sentiment analysis of personal opinions",
            "reference": "https://vlsp.org.vn/vlsp2016/eval/sa",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["vi"],
            "main_score": "f1",
        }