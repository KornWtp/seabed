from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class TagalogFakenewsClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "TagalogFakenewsTextClassification",
            "hf_hub_name": "kornwtp/tl-fake-news-classification",
            "description": "Fake News Detection Corpora in Filipino.",
            "reference": "https://huggingface.co/datasets/jcblaise/fake_news_filipino",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["tl"],
            "main_score": "f1",
        }