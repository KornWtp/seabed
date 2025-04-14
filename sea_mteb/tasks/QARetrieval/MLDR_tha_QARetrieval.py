from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class MLDR_tha_QARetrieval(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "MLDR_tha_QARetrieval",
            "hf_hub_name": "kornwtp/mldr-tha-qaretrieval",
            "description": "Thai document retrieval from Multilingual Long-Document Retrieval dataset.",
            "reference": "https://huggingface.co/datasets/Shitao/MLDR",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["test"],
            "eval_langs": ["tha"],
            "main_score": "ndcg@k",
        }