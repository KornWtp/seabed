from ...abstasks.AbsTaskPairClassification import AbsTaskPairClassification


class SQuADNLI_ind_PairClassification(AbsTaskPairClassification):
    @property
    def description(self):
        return {
            "name": "SQuADNLI_ind_PairClassification",
            "hf_hub_name": "kornwtp/squad-nli-ind-pairclassification",
            "description": "Sentence pairs classification is derived from the SQuAD-ID question answering dataset, designed to facilitate Natural Language Inference (NLI) tasks.",
            "reference": "https://huggingface.co/datasets/muhammadravi251001/squadid-nli",
            "category": "s2s",
            "type": "PairClassification",
            "eval_splits": ["test"],
            "eval_langs": ["ind"],
            "main_score": "ap",
        }