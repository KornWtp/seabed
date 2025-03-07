from ...abstasks.AbsTaskClassification import AbsTaskClassification


class The40ThaiChildrenStories_tha_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "The40ThaiChildrenStories_tha_Classification",
            "hf_hub_name": "kornwtp/the40thai-children-stories-tha-classification",
            "description": "Text classification collected from 40 Thai children stories.",
            "reference": "https://github.com/dsmlr/40-Thai-Children-Stories",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["tha"],
            "main_score": "f1",
        }