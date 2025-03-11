from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class ContextSearch_vie_QARetrieval(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "ContextSearch_vie_QARetrieval",
            "hf_hub_name": "kornwtp/context-search-vie-qaretrieval",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["validation"],
            "eval_langs": ["vie"],
            "main_score": "ndcg@k",
        }