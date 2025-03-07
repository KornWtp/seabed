from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class IndoNLG_ind_QARetrieval(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "IndoNLG_ind_QARetrieval",
            "hf_hub_name": "kornwtp/indonlg-ind-qaretrieval",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["test"],
            "eval_langs": ["ind"],
            "main_score": "ndcg@k",
        }