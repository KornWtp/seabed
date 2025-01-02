from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class IndoClickbaitClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "IndoClickbaitClassification",
            "hf_hub_name": "kornwtp/id-clickbait",
            "description": "Indonesian news headlines for text classification",
            "reference": "https://data.mendeley.com/datasets/k42j7x2kpn/1",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "f1",
        }