from ...abstasks.AbsTaskClassification import AbsTaskClassification


class Depression_tha_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "Depression_tha_Classification",
            "hf_hub_name": "kornwtp/depression-tha-classification",
            "description": "Thai text classification",
            "reference": "https://huggingface.co/datasets/SEACrowd/thai_depression",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["tha"],
            "main_score": "f1",
        }