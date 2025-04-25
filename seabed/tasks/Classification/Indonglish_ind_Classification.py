from ...abstasks.AbsTaskClassification import AbsTaskClassification


class Indonglish_ind_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "Indonglish_ind_Classification",
            "hf_hub_name": "kornwtp/indonglish-ind-classification",
            "description": "Indonglish-dataset was constructed based on keywords derived from the sociolinguistic phenomenon observed among teenagers in South Jakarta.",
            "reference": "https://github.com/laksmitawidya/indonglish-dataset",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["ind"],
            "main_score": "f1",
        }