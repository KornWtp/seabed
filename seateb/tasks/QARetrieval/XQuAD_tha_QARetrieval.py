from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class XQuAD_tha_QARetrieval(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "XQuAD_tha_QARetrieval",
            "hf_hub_name": "kornwtp/xquad-tha-qaretrieval",
            "description": "Cross-lingual question answering.",
            "reference": "https://huggingface.co/datasets/google/xquad",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["validation"],
            "eval_langs": ["tha"],
            "main_score": "ndcg@k",
        }