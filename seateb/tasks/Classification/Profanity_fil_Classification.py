from ...abstasks.AbsTaskClassification import AbsTaskClassification


class Profanity_fil_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "Profanity_fil_Classification",
            "hf_hub_name": "kornwtp/profanity-fil-dataset",
            "description": "Text classification from Tagalog profanity dataset.",
            "reference": "https://huggingface.co/datasets/mginoben/tagalog-profanity-dataset",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["fil"],
            "main_score": "f1",
        }