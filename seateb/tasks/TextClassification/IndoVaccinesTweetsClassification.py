from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class IndoVaccinesTweetsClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "IndoVaccinesTweetsClassification",
            "hf_hub_name": "kornwtp/id-vaccines-tweets-classification",
            "description": "Dataset containing tweets about COVID-19 vaccines with manually labelled information about whether they are a subjective tweet and their sentiment polarity.",
            "reference": "https://github.com/rayendito/id-vaccines-tweets",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "f1",
        }