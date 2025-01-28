from ...abstasks.AbsTaskMultiLabelTextClassification import AbsTaskMultiLabelTextClassification


class IndoNetifierMultiLabelClassification(AbsTaskMultiLabelTextClassification):
    @property
    def description(self):
        return {
            "name": "IndoNetifierMultiLabelClassification",
            "hf_hub_name": "kornwtp/id_multilabel_hatespeech",
            "description": "Multilabel text classification from Indonesian social media text toxicity",
            "reference": "https://github.com/ahmadizzan/netifier",
            "category": "s2s",
            "type": "MultiLabelTextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "f1",
        }