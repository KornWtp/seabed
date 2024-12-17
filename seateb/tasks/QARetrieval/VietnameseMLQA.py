from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class VietnameseMLQA(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "VietnameseMLQA",
            "hf_hub_name": "kornwtp/vi-mlqa",
            "description": "Question answering from MultiLingual Question Answering dataset.",
            "reference": "https://github.com/facebookresearch/MLQA",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["test"],
            "eval_langs": ["vi"],
            "main_score": "mrr",
        }