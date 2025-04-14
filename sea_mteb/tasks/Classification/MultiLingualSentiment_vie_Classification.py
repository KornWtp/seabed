from ...abstasks.AbsTaskClassification import AbsTaskClassification


class MultiLingualSentiment_vie_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "MultiLingualSentiment_vie_Classification",
            "hf_hub_name": "kornwtp/multilingual-sentiment-vie-classification",
            "description": "Sentiment classification from multilingual sentiment classification datasets.",
            "reference": "https://huggingface.co/datasets/mteb/multilingual-sentiment-classification",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["vie"],
            "main_score": "f1",
        }