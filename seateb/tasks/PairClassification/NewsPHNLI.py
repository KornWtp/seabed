from ...abstasks.AbsTaskPairClassification import AbsTaskPairClassification


class NewsPHNLI(AbsTaskPairClassification):
    @property
    def description(self):
        return {
            "name": "NewsPHNLI",
            "hf_hub_name": "kornwtp/newsph_nli",
            "description": "Sentence pairs classification in the low-resource Filipino language.",
            "reference": "https://huggingface.co/datasets/jcblaise/newsph_nli",
            "category": "s2s",
            "type": "PairClassification",
            "eval_splits": ["validation", "test"],
            "eval_langs": ["fil"],
            "main_score": "ap",
        }