from ...abstasks.AbsTaskClassification import AbsTaskClassification


class LEMSentiment_ind_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "LEMSentiment_ind_Classification",
            "hf_hub_name": "kornwtp/lem-sentiment-ind-classification",
            "description": "IndoLEM (Indonesian Language Evaluation Montage) is a comprehensive Indonesian benchmark that comprises of seven tasks for the Indonesian language.",
            "reference": "https://huggingface.co/datasets/SEACrowd/indolem_sentiment",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["ind"],
            "main_score": "f1",
        }