from ...abstasks.AbsTaskClassification import AbsTaskClassification


class ViOCD_vie_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "ViOCD_vie_Classification",
            "hf_hub_name": "kornwtp/viocd-vie-classification",
            "description": "Vietnamese Open-Domain Complaint Detection in E-commerce Websites",
            "reference": "https://huggingface.co/datasets/tarudesu/ViOCD",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["vie"],
            "main_score": "f1",
        }