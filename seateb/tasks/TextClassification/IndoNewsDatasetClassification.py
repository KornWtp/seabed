from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class IndoNewsDatasetClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "IndoNewsDatasetClassification",
            "hf_hub_name": "kornwtp/id-news-dataset-classification",
            "description": "An imbalanced dataset to classify Indonesian News articles.",
            "reference": "https://github.com/andreaschandra/indonesian-news",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "f1",
        }