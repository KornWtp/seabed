from ...abstasks.AbsTaskPairClassification import AbsTaskPairClassification


class NewsPHNLI_fil_PairClassification(AbsTaskPairClassification):
    @property
    def description(self):
        return {
            "name": "NewsPHNLI_fil_PairClassification",
            "hf_hub_name": "kornwtp/newsph-nli-fil-pairclassification",
            "description": "Sentence pairs classification in the low-resource Filipino language.",
            "reference": "https://huggingface.co/datasets/jcblaise/newsph_nli",
            "category": "s2s",
            "type": "PairClassification",
            "eval_splits": ["test"],
            "eval_langs": ["fil"],
            "main_score": "ap",
        }