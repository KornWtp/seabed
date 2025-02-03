from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class IndoSentEmoMobileAppsClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "IndoSentEmoMobileAppsClassification",
            "hf_hub_name": "kornwtp/id-sent-emo-mobile-apps-classification",
            "description": "This dataset contains manually annotated public reviews of mobile applications in Indonesia.",
            "reference": "https://github.com/Ricco48/Multilabel-Sentiment-and-Emotion-Dataset-from-Indonesian-Mobile-Application-Review/tree/CreateCodeForPaper",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "f1",
        }