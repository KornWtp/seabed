from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class IndoMinangClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "IndoMinangClassification",
            "hf_hub_name": "kornwtp/id-minang-classification",
            "description": "The Minangkabau corpus is sentiment analysis by manually translating 5,000 sentences of Indonesian sentiment analysis corpora.",
            "reference": "https://github.com/fajri91/minangNLP",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "f1",
        }