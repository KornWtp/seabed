from ...abstasks.AbsTaskMultiLabelTextClassification import AbsTaskMultiLabelTextClassification


class IndoCASA(AbsTaskMultiLabelTextClassification):
    @property
    def description(self):
        return {
            "name": "IndoCASAMultiLabelTextClassification",
            "hf_hub_name": "kornwtp/indonlu-casa",
            "description": "Multilabel text classification from various Indonesian online automobile platforms.",
            "reference": "https://huggingface.co/datasets/indonlp/indonlu",
            "category": "s2s",
            "type": "MultiLabelTextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "f1",
        }