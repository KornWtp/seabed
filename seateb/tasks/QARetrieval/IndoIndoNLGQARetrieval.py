from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class IndoIndoNLGQARetrieval(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "IndoIndoNLGQARetrieval",
            "hf_hub_name": "kornwtp/id-indonlg-retrieval",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "ndcg@k",
        }