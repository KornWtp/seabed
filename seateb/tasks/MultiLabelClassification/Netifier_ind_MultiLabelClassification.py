from ...abstasks.AbsTaskMultiLabelClassification import AbsTaskMultiLabelClassification


class Netifier_ind_MultiLabelClassification(AbsTaskMultiLabelClassification):
    @property
    def description(self):
        return {
            "name": "Netifier_ind_MultiLabelClassification",
            "hf_hub_name": "kornwtp/netifier-ind-multilabelclassification",
            "description": "Multilabel text classification from Indonesian social media text toxicity",
            "reference": "https://github.com/ahmadizzan/netifier",
            "category": "s2s",
            "type": "MultiLabelClassification",
            "eval_splits": ["test"],
            "eval_langs": ["ind"],
            "main_score": "f1",
        }