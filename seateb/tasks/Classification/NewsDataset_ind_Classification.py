from ...abstasks.AbsTaskClassification import AbsTaskClassification


class NewsDataset_ind_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "NewsDataset_ind_Classification",
            "hf_hub_name": "kornwtp/newsdataset-ind-classification",
            "description": "An imbalanced dataset to classify Indonesian News articles.",
            "reference": "https://github.com/andreaschandra/indonesian-news",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["ind"],
            "main_score": "f1",
        }