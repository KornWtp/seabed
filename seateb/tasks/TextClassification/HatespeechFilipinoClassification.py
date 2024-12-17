from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class HatespeechFilipinoClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "HatespeechFilipinoClassification",
            "hf_hub_name": "kornwtp/hatespeech-filipino",
            "description": "Text Classification Dataset in Filipino",
            "reference": "https://huggingface.co/datasets/jcblaise/hatespeech_filipino",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["tl"],
            "main_score": "f1",
        }