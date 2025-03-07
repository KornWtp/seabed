from ...abstasks.AbsTaskClassification import AbsTaskClassification


class HoaxNews_ind_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "HoaxNews_ind_Classification",
            "hf_hub_name": "kornwtp/hoaxnews-ind-classfication",
            "description": "Indonesian Hoax news headlines for text classification",
            "reference": "https://data.mendeley.com/datasets/p3hfgr5j3m/1",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["ind"],
            "main_score": "f1",
        }