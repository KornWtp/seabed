from ...abstasks.AbsTaskClassification import AbsTaskClassification


class EmotCMT_ind_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "EmotCMT_ind_Classification",
            "hf_hub_name": "kornwtp/emotcmt-ind-classification",
            "description": "EmotCMT is an emotion classification Indonesian-English code-mixing dataset created through an Indonesian-English code-mixed Twitter data pipeline consisting of 4 processing steps, i.e., tokenization, language identification, lexical normalization, and translation.",
            "reference": "https://github.com/ir-nlp-csui/emotcmt",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["ind"],
            "main_score": "f1",
        }