from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class IndoEmotCMTClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "IndoEmotCMTClassification",
            "hf_hub_name": "kornwtp/id-emotcmt-classification",
            "description": "EmotCMT is an emotion classification Indonesian-English code-mixing dataset created through an Indonesian-English code-mixed Twitter data pipeline consisting of 4 processing steps, i.e., tokenization, language identification, lexical normalization, and translation.",
            "reference": "https://github.com/ir-nlp-csui/emotcmt",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "f1",
        }