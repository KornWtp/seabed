from ...abstasks.AbsTaskMultiLabelClassification import AbsTaskMultiLabelClassification


class Dengue_fil_MultiLabelClassification(AbsTaskMultiLabelClassification):
    @property
    def description(self):
        return {
            "name": "Dengue_fil_MultiLabelClassification",
            "hf_hub_name": "kornwtp/dengue-fil-multilabelclassification",
            "description": "Multilabel text classification from Dengue dataset in Filipino.",
            "reference": "https://huggingface.co/datasets/jcblaise/dengue_filipino",
            "category": "s2s",
            "type": "MultiLabelClassification",
            "eval_splits": ["test"],
            "eval_langs": ["fil"],
            "main_score": "f1",
        }