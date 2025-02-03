from ...abstasks.AbsTaskPairClassification import AbsTaskPairClassification


class IndoSQuADNLIPairClassification(AbsTaskPairClassification):
    @property
    def description(self):
        return {
            "name": "IndoSQuADNLIPairClassification",
            "hf_hub_name": "kornwtp/id-squad-nli",
            "description": "Sentence pairs classification is derived from the SQuAD-ID question answering dataset, designed to facilitate Natural Language Inference (NLI) tasks.",
            "reference": "https://huggingface.co/datasets/muhammadravi251001/squadid-nli",
            "category": "s2s",
            "type": "PairClassification",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "ap",
        }