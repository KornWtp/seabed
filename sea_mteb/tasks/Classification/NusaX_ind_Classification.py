from ...abstasks.AbsTaskClassification import AbsTaskClassification


class NusaX_ind_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "NusaX_ind_Classification",
            "hf_hub_name": "kornwtp/nusax-ind-classification",
            "description": "NusaX-Senti is a 3-labels (positive, neutral, negative) sentiment analysis dataset for 10 Indonesian local languages + Indonesian and English.",
            "reference": "https://github.com/IndoNLP/nusax/tree/main/datasets/sentiment",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["ind"],
            "main_score": "f1",
        }