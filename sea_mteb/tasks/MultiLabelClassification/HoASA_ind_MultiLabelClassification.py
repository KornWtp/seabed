from ...abstasks.AbsTaskMultiLabelClassification import AbsTaskMultiLabelClassification


class HoASA_ind_MultiLabelClassification(AbsTaskMultiLabelClassification):
    @property
    def description(self):
        return {
            "name": "HoASA_ind_MultiLabelClassification",
            "hf_hub_name": "kornwtp/hoasa-ind-multilabelclassification",
            "description": "Multilabel text classification from Indonesian hotel reviews.",
            "reference": "https://huggingface.co/datasets/indonlp/indonlu",
            "category": "s2s",
            "type": "MultiLabelClassification",
            "eval_splits": ["test"],
            "eval_langs": ["ind"],
            "main_score": "f1",
        }