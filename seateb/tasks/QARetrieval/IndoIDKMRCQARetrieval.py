from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class IndoIDKMRCQARetrieval(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "IndoIDKMRCQARetrieval",
            "hf_hub_name": "kornwtp/id-idkmrc",
            "description": "I(n)dontKnow-MRC (IDK-MRC) is an Indonesian Machine Reading Comprehension dataset that covers answerable and unanswerable questions.",
            "reference": "https://github.com/rifkiaputri/IDK-MRC",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "ndcg@k",
        }