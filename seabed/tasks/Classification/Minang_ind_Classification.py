from ...abstasks.AbsTaskClassification import AbsTaskClassification


class Minang_ind_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "Minang_ind_Classification",
            "hf_hub_name": "kornwtp/minang-ind-classification",
            "description": "The Minangkabau corpus is sentiment analysis by manually translating 5,000 sentences of Indonesian sentiment analysis corpora.",
            "reference": "https://github.com/fajri91/minangNLP",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["ind"],
            "main_score": "f1",
        }