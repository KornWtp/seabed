from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class BurmeseGKLMIPSentimentClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "BurmeseGKLMIPSentimentClassification",
            "hf_hub_name": "kornwtp/burmese-gklmip-sentiment",
            "description": "Myanmar news corpus is intended for training and evaluation of text classification tasks for the Myanmar language.",
            "reference": "https://github.com/GKLMIP/Pretrained-Models-For-Myanmar",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["my"],
            "main_score": "f1",
        }