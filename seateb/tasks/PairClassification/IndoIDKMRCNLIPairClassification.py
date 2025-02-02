from ...abstasks.AbsTaskPairClassification import AbsTaskPairClassification


class IndoIDKMRCNLIPairClassification(AbsTaskPairClassification):
    @property
    def description(self):
        return {
            "name": "IndoIDKMRCNLIPairClassification",
            "hf_hub_name": "kornwtp/id-idkmrc-nli",
            "description": "Sentence pairs classification is derived from the IDK-MRC question answering dataset, designed to facilitate Natural Language Inference (NLI) tasks.",
            "reference": "https://huggingface.co/datasets/muhammadravi251001/idkmrc-nli",
            "category": "s2s",
            "type": "PairClassification",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "ap",
        }