from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class VietnameseViOCDClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "VietnameseViOCDClassification",
            "hf_hub_name": "kornwtp/ViOCD-classification",
            "description": "Vietnamese Open-Domain Complaint Detection in E-commerce Websites",
            "reference": "https://huggingface.co/datasets/tarudesu/ViOCD",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["vi"],
            "main_score": "f1",
        }