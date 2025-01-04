from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class ViQuAD2_0(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "ViQuAD2_0",
            "hf_hub_name": "kornwtp/UIT-ViQuAD2.0",
            "description": "Vietnamese Question Answering dataset.",
            "reference": "https://huggingface.co/datasets/taidng/UIT-ViQuAD2.0",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["test"],
            "eval_langs": ["vi"],
            "main_score": "mrr",
        }