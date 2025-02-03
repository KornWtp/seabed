from ...abstasks.AbsTaskMultiLabelTextClassification import AbsTaskMultiLabelTextClassification


class IndoHateSpeechMultiLabelClassification(AbsTaskMultiLabelTextClassification):
    @property
    def description(self):
        return {
            "name": "IndoHateSpeechMultiLabelClassification",
            "hf_hub_name": "kornwtp/id_multilabel_hatespeech",
            "description": "Multilabel text classification from Indonesian Twitter",
            "reference": "https://github.com/okkyibrohim/id-multi-label-hate-speech-and-abusive-language-detection",
            "category": "s2s",
            "type": "MultiLabelTextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "f1",
        }