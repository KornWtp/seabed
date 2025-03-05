from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class IAppWiki_tha_QARetrieval(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "IAppWiki_tha_QARetrieval",
            "hf_hub_name": "kornwtp/iapp-wikiqa-tha-qaretrieval",
            "description": "iapp_wiki_qa_squad is an extractive question answering dataset from Thai Wikipedia articles.",
            "reference": "https://huggingface.co/datasets/iapp/iapp_wiki_qa_squad",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["test"],
            "eval_langs": ["tha"],
            "main_score": "ndcg@k",
        }