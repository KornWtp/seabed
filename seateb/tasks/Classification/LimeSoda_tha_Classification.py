from ...abstasks.AbsTaskClassification import AbsTaskClassification


class LimeSoda_tha_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "LimeSoda_tha_Classification",
            "hf_hub_name": "kornwtp/limesoda-tha-classification",
            "description": "Thai fake news dataset in the healthcare domain",
            "reference": "https://github.com/byinth/LimeSoda",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["tha"],
            "main_score": "f1",
        }