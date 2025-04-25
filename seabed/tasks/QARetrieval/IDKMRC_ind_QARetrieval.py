from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class IDKMRC_ind_QARetrieval(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "IDKMRC_ind_QARetrieval",
            "hf_hub_name": "kornwtp/idkmrc-ind-qaretrieval",
            "description": "I(n)dontKnow-MRC (IDK-MRC) is an Indonesian Machine Reading Comprehension dataset that covers answerable and unanswerable questions.",
            "reference": "https://github.com/rifkiaputri/IDK-MRC",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["test"],
            "eval_langs": ["ind"],
            "main_score": "ndcg@k",
        }