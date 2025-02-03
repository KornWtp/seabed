from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class IndoHateSpeechClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "IndoHateSpeechClassification",
            "hf_hub_name": "kornwtp/id-hatespeech-classification",
            "description": "The ID Hatespeech dataset is collection of 713 tweets related to a political event, the Jakarta Governor Election 2017 designed for hate speech detection NLP task.",
            "reference": "https://huggingface.co/datasets/SEACrowd/id_hatespeech",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "f1",
        }