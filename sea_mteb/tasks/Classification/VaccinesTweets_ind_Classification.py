from ...abstasks.AbsTaskClassification import AbsTaskClassification


class VaccinesTweets_ind_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "VaccinesTweets_ind_Classification",
            "hf_hub_name": "kornwtp/vaccines-tweets-ind-classification",
            "description": "Dataset containing tweets about COVID-19 vaccines with manually labelled information about whether they are a subjective tweet and their sentiment polarity.",
            "reference": "https://github.com/rayendito/id-vaccines-tweets",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["ind"],
            "main_score": "f1",
        }