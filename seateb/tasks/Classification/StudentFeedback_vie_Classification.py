from ...abstasks.AbsTaskClassification import AbsTaskClassification


class StudentFeedback_vie_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "StudentFeedback_vie_Classification",
            "hf_hub_name": "kornwtp/students-feedback-vie-classification",
            "description": "Text classification from Vietnamese Students’ Feedback Corpus.",
            "reference": "https://huggingface.co/datasets/uitnlp/vietnamese_students_feedback",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["vie"],
            "main_score": "f1",
        }