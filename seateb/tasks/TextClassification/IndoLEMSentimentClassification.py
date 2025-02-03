from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class IndoLEMSentimentClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "IndoLEMSentimentClassification",
            "hf_hub_name": "kornwtp/id-lem-sentiment-classification",
            "description": "IndoLEM (Indonesian Language Evaluation Montage) is a comprehensive Indonesian benchmark that comprises of seven tasks for the Indonesian language.",
            "reference": "https://huggingface.co/datasets/SEACrowd/indolem_sentiment",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "f1",
        }