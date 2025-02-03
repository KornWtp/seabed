from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class IndoNusaXClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "IndoNusaXClassification",
            "hf_hub_name": "kornwtp/id-nusax-classification",
            "description": "NusaX-Senti is a 3-labels (positive, neutral, negative) sentiment analysis dataset for 10 Indonesian local languages + Indonesian and English.",
            "reference": "https://github.com/IndoNLP/nusax/tree/main/datasets/sentiment",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "f1",
        }