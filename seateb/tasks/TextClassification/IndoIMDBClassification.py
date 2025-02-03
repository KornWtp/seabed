from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class IndoIMDBClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "IndoIMDBClassification",
            "hf_hub_name": "kornwtp/id-imdb-jv-classification",
            "description": "Javanese Imdb Movie Reviews Dataset is a Javanese version of the IMDb Movie Reviews dataset by translating the original English dataset to Javanese.",
            "reference": "https://huggingface.co/datasets/w11wo/imdb-javanese",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "f1",
        }