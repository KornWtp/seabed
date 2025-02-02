from ...abstasks.AbsTaskPairClassification import AbsTaskPairClassification


class IndoTyDIQANLIPairClassification(AbsTaskPairClassification):
    @property
    def description(self):
        return {
            "name": "IndoTyDIQANLIPairClassification",
            "hf_hub_name": "kornwtp/id-tydiqa-nli",
            "description": "Sentence pairs classification is derived from the TyDI-QA-ID question answering dataset, designed to facilitate Natural Language Inference (NLI) tasks.",
            "reference": "https://huggingface.co/datasets/muhammadravi251001/tydiqaid-nli",
            "category": "s2s",
            "type": "PairClassification",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "ap",
        }