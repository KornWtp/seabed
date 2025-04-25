from ...abstasks.AbsTaskClassification import AbsTaskClassification


class Clickbait_ind_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "Clickbait_ind_Classification",
            "hf_hub_name": "kornwtp/clickbait-ind-classification",
            "description": "Indonesian news headlines for text classification",
            "reference": "https://data.mendeley.com/datasets/k42j7x2kpn/1",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["ind"],
            "main_score": "f1",
        }