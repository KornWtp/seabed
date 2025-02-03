from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class EMoTES3KClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "EMoTES3KClassification",
            "hf_hub_name": "kornwtp/EMoTES-3K",
            "description": "This English-Filipino parallel corpus contains moral judgments and explanations of various day-to-day scenarios.",
            "reference": "https://huggingface.co/datasets/NLPinas/EMoTES-3K",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["tl"],
            "main_score": "f1",
        }