from ...abstasks.AbsTaskMultiLabelTextClassification import AbsTaskMultiLabelTextClassification


class Dengue(AbsTaskMultiLabelTextClassification):
    @property
    def description(self):
        return {
            "name": "Dengue",
            "hf_hub_name": "kornwtp/dengue-filipino",
            "description": "Multilabel text classification from Dengue dataset in Filipino.",
            "reference": "https://huggingface.co/datasets/jcblaise/dengue_filipino",
            "category": "s2s",
            "type": "MultiLabelTextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["tl"],
            "main_score": "f1",
        }