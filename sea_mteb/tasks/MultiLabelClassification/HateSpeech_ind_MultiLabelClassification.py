from ...abstasks.AbsTaskMultiLabelClassification import AbsTaskMultiLabelClassification


class HateSpeech_ind_MultiLabelClassification(AbsTaskMultiLabelClassification):
    @property
    def description(self):
        return {
            "name": "HateSpeech_ind_MultiLabelClassification",
            "hf_hub_name": "kornwtp/hatespeech-ind-multilabelclassification",
            "description": "Multilabel text classification from Indonesian Twitter",
            "reference": "https://github.com/okkyibrohim/id-multi-label-hate-speech-and-abusive-language-detection",
            "category": "s2s",
            "type": "MultiLabelClassification",
            "eval_splits": ["test"],
            "eval_langs": ["ind"],
            "main_score": "f1",
        }