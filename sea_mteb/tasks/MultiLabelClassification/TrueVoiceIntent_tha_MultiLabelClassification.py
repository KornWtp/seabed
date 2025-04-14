from ...abstasks.AbsTaskMultiLabelClassification import AbsTaskMultiLabelClassification


class TrueVoiceIntent_tha_MultiLabelClassification(AbsTaskMultiLabelClassification):
    @property
    def description(self):
        return {
            "name": "TrueVoiceIntent_tha_MultiLabelClassification",
            "hf_hub_name": "kornwtp/truevoice-intent-tha-multilabelclassification",
            "description": "Thai multilabel text classification from TrueVoice.",
            "reference": "https://github.com/PyThaiNLP/truevoice-intent",
            "category": "s2s",
            "type": "MultiLabelClassification",
            "eval_splits": ["test"],
            "eval_langs": ["tha"],
            "main_score": "f1",
        }