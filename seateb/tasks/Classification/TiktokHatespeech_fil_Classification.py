from ...abstasks.AbsTaskClassification import AbsTaskClassification


class TiktokHatespeech_fil_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "TiktokHatespeech_fil_Classification",
            "hf_hub_name": "kornwtp/tiktok-hatespeech-fil-classification",
            "description": "This corpus contains the hate speech text dataset from the paper A BERT-based Hate Speech Classifier from Transcribed Online Short-Form Videos transcribed from collected videos from Tiktok.",
            "reference": "https://github.com/imperialite/filipino-tiktok-hatespeech/tree/main",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["fil"],
            "main_score": "f1",
        }