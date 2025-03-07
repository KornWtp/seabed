from ...abstasks.AbsTaskClassification import AbsTaskClassification


class Hatespeech_fil_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "Hatespeech_fil_Classification",
            "hf_hub_name": "kornwtp/hatespeech-fil-classification",
            "description": "Text Classification Dataset in Filipino",
            "reference": "https://huggingface.co/datasets/jcblaise/hatespeech_filipino",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["fil"],
            "main_score": "f1",
        }