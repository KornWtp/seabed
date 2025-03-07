from ...abstasks.AbsTaskClassification import AbsTaskClassification


class Fakenews_fil_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "Fakenews_fil_Classification",
            "hf_hub_name": "kornwtp/fakenews-fil-classification",
            "description": "Fake News Detection Corpora in Filipino.",
            "reference": "https://huggingface.co/datasets/jcblaise/fake_news_filipino",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["fil"],
            "main_score": "f1",
        }