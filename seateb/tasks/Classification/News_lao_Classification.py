from ...abstasks.AbsTaskClassification import AbsTaskClassification


class News_lao_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "News_lao_Classification",
            "hf_hub_name": "kornwtp/news-lao-classification",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["lao"],
            "main_score": "f1",
        }