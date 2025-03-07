from ...abstasks.AbsTaskClassification import AbsTaskClassification


class SentEmoMobileApps_ind_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "SentEmoMobileApps_ind_Classification",
            "hf_hub_name": "kornwtp/sentiment-emo-mobileapps-ind-classification",
            "description": "This dataset contains manually annotated public reviews of mobile applications in Indonesia.",
            "reference": "https://github.com/Ricco48/Multilabel-Sentiment-and-Emotion-Dataset-from-Indonesian-Mobile-Application-Review/tree/CreateCodeForPaper",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["ind"],
            "main_score": "f1",
        }