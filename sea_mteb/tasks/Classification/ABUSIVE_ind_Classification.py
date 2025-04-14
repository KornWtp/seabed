from ...abstasks.AbsTaskClassification import AbsTaskClassification


class ABUSIVE_ind_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "ABUSIVE_ind_Classification",
            "hf_hub_name": "kornwtp/abusive-ind-classification",
            "description": "The ID_ABUSIVE dataset is collection of 2,016 informal abusive tweets in Indonesian language, designed for sentiment analysis NLP task.",
            "reference": "https://github.com/dadelani/sib-200",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["ind"],
            "main_score": "f1",
        }