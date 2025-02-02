from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class ThaiWikiQAQARetrieval(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "ThaiWikiQAQARetrieval",
            "hf_hub_name": "kornwtp/thai-wiki-qa",
            "description": "Thai Wiki QA dataset is an open domain Q&A dataset created from documents on Thai Wikipedia.",
            "reference": "https://aiforthai.in.th/",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["train"],
            "eval_langs": ["th"],
            "main_score": "ndcg@k",
        }