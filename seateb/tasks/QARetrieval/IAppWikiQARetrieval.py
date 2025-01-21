from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class IAppWikiQARetrieval(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "IAppWikiQARetrieval",
            "hf_hub_name": "kornwtp/iapp_wiki_qa_squad",
            "description": "iapp_wiki_qa_squad is an extractive question answering dataset from Thai Wikipedia articles.",
            "reference": "https://huggingface.co/datasets/iapp/iapp_wiki_qa_squad",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["test"],
            "eval_langs": ["th"],
            "main_score": "ndcg@k",
        }