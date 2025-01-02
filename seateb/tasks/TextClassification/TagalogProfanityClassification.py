from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class TagalogProfanityClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "TagalogProfanityClassification",
            "hf_hub_name": "kornwtp/tl-profanity-dataset",
            "description": "Text classification from Tagalog profanity dataset.",
            "reference": "https://huggingface.co/datasets/mginoben/tagalog-profanity-dataset",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["tl"],
            "main_score": "f1",
        }