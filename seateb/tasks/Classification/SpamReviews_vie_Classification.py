from ...abstasks.AbsTaskClassification import AbsTaskClassification


class SpamReviews_vie_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "SpamReviews_vie_Classification",
            "hf_hub_name": "kornwtp/spam-reviews-vie-classification",
            "description": "The dataset was collected from leading online shopping platforms in Vietnam. Some of the most recent selling products for each product category were selected and up to 15 reviews per product were collected.",
            "reference": "https://github.com/sonlam1102/vispamdetection",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["vie"],
            "main_score": "f1",
        }