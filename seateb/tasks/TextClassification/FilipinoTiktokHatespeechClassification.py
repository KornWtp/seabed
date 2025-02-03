from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class FilipinoTiktokHatespeechClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "FilipinoTiktokHatespeechClassification",
            "hf_hub_name": "kornwtp/filipino-tiktok-hatespeech-classification",
            "description": "This corpus contains the hate speech text dataset from the paper A BERT-based Hate Speech Classifier from Transcribed Online Short-Form Videos transcribed from collected videos from Tiktok.",
            "reference": "https://github.com/imperialite/filipino-tiktok-hatespeech/tree/main",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["tl"],
            "main_score": "f1",
        }