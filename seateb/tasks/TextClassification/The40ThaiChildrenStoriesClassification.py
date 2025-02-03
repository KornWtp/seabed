from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class The40ThaiChildrenStoriesClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "The40ThaiChildrenStoriesClassification",
            "hf_hub_name": "kornwtp/the-40-thai-children-stories-classification",
            "description": "Text classification collected from 40 Thai children stories.",
            "reference": "https://github.com/dsmlr/40-Thai-Children-Stories",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["th"],
            "main_score": "f1",
        }