from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class IndoAbusiveNewsCommentClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "IndoAbusiveNewsCommentClassification",
            "hf_hub_name": "kornwtp/id-abusive-news-comment-classification",
            "description": "Abusive language is an expression used by a person with insulting delivery of any person's aspect. In the modern era, the use of harsh words is often found on the internet, one of them is in the comment section of online news articles which contains harassment, insult, or a curse.",
            "reference": "https://github.com/dhamirdesrul/Indonesian-Online-News-Comments",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "f1",
        }