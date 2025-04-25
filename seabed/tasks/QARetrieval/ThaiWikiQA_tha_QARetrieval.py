from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class ThaiWikiQA_ind_QARetrieval(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "ThaiWikiQA_tha_QARetrieval",
            "hf_hub_name": "kornwtp/thai-wikiqa-tha-qaretrieval",
            "description": "Thai Wiki QA dataset is an open domain Q&A dataset created from documents on Thai Wikipedia.",
            "reference": "https://aiforthai.in.th/",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["train"],
            "eval_langs": ["tha"],
            "main_score": "ndcg@k",
        }