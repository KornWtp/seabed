from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class IndoHoaxNewsClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "IndoHoaxNewsClassification",
            "hf_hub_name": "kornwtp/id-hoax-news-classfication",
            "description": "Indonesian Hoax news headlines for text classification",
            "reference": "https://data.mendeley.com/datasets/p3hfgr5j3m/1",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "f1",
        }