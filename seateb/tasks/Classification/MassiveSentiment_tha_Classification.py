from ...abstasks.AbsTaskClassification import AbsTaskClassification


class MassiveSentiment_tha_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "MassiveSentiment_tha_Classification",
            "hf_hub_name": "kornwtp/massive-sentiment-tha-classification",
            "description": "Sentiment classification from multilingual sentiment classification datasets.",
            "reference": "https://huggingface.co/datasets/mteb/multilingual-sentiment-classification",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["tha"],
            "main_score": "f1",
        }