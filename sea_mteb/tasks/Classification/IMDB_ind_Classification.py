from ...abstasks.AbsTaskClassification import AbsTaskClassification


class IMDB_ind_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "IMDB_ind_Classification",
            "hf_hub_name": "kornwtp/imdb-ind-classification",
            "description": "Javanese Imdb Movie Reviews Dataset is a Javanese version of the IMDb Movie Reviews dataset by translating the original English dataset to Javanese.",
            "reference": "https://huggingface.co/datasets/w11wo/imdb-javanese",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["ind"],
            "main_score": "f1",
        }