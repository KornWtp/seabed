from ...abstasks.AbsTaskMultiLabelTextClassification import AbsTaskMultiLabelTextClassification


class IndoHoASA(AbsTaskMultiLabelTextClassification):
    @property
    def description(self):
        return {
            "name": "IndoHoASA",
            "hf_hub_name": "kornwtp/indonlu-hoasa",
            "description": "Multilabel text classification from Indonesian hotel reviews.",
            "reference": "https://huggingface.co/datasets/indonlp/indonlu",
            "category": "s2s",
            "type": "MultiLabelTextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "f1",
        }