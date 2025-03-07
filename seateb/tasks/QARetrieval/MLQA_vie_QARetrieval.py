from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class MLQA_vie_QARetrieval(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "MLQA_vie_QARetrieval",
            "hf_hub_name": "kornwtp/mlqa-vie-qaretrieval",
            "description": "Question answering from MultiLingual Question Answering dataset.",
            "reference": "https://github.com/facebookresearch/MLQA",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["test"],
            "eval_langs": ["vie"],
            "main_score": "ndcg@k",
        }