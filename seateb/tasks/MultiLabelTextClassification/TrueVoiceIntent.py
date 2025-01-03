from ...abstasks.AbsTaskMultiLabelTextClassification import AbsTaskMultiLabelTextClassification


class TrueVoiceIntent(AbsTaskMultiLabelTextClassification):
    @property
    def description(self):
        return {
            "name": "TrueVoiceIntent",
            "hf_hub_name": "kornwtp/truevoice-intent",
            "description": "Thai multilabel text classification from TrueVoice.",
            "reference": "https://github.com/PyThaiNLP/truevoice-intent",
            "category": "s2s",
            "type": "MultiLabelTextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["th"],
            "main_score": "f1",
        }