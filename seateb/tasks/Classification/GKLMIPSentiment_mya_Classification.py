from ...abstasks.AbsTaskClassification import AbsTaskClassification


class GKLMIPSentiment_mya_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "GKLMIPSentiment_mya_Classification",
            "hf_hub_name": "kornwtp/gklmip-sentiment-mya-classification",
            "description": "Myanmar news corpus is intended for training and evaluation of text classification tasks for the Myanmar language.",
            "reference": "https://github.com/GKLMIP/Pretrained-Models-For-Myanmar",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["mya"],
            "main_score": "f1",
        }