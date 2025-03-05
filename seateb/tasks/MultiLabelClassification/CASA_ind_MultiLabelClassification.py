from ...abstasks.AbsTaskMultiLabelClassification import AbsTaskMultiLabelClassification


class CASA_ind_MultiLabelClassification(AbsTaskMultiLabelClassification):
    @property
    def description(self):
        return {
            "name": "CASA_ind_MultiLabelClassification",
            "hf_hub_name": "kornwtp/casa-ind-multilabelclassification",
            "description": "Multilabel text classification from various Indonesian online automobile platforms.",
            "reference": "https://huggingface.co/datasets/indonlp/indonlu",
            "category": "s2s",
            "type": "MultiLabelClassification",
            "eval_splits": ["test"],
            "eval_langs": ["ind"],
            "main_score": "f1",
        }