from ...abstasks.AbsTaskClassification import AbsTaskClassification


class EMoTES3K_fil_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "EMoTES3K_fil_Classification",
            "hf_hub_name": "kornwtp/emotes3k-fil-classification",
            "description": "This English-Filipino parallel corpus contains moral judgments and explanations of various day-to-day scenarios.",
            "reference": "https://huggingface.co/datasets/NLPinas/EMoTES-3K",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["fil"],
            "main_score": "f1",
        }