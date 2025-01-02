from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class VietnameseStudentFeedbackClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "VietnameseStudentFeedbackClassification",
            "hf_hub_name": "kornwtp/vi-students-feedback",
            "description": "Text classification from Vietnamese Students’ Feedback Corpus.",
            "reference": "https://huggingface.co/datasets/uitnlp/vietnamese_students_feedback",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["vi"],
            "main_score": "f1",
        }