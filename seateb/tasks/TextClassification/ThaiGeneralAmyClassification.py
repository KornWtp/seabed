from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class ThaiGeneralAmyClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "ThaiGeneralAmyClassification",
            "hf_hub_name": "kornwtp/general-amy-classification",
            "description": "Thai text classification",
            "reference": "https://github.com/PyThaiNLP/thai-sentiment-analysis-dataset",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["th"],
            "main_score": "f1",
        }