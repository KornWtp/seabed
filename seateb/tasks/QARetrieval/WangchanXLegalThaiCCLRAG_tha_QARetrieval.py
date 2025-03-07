from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class WangchanXLegalThaiCCLRAG_tha_QARetrieval(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "WangchanXLegalThaiCCLRAG_tha_QARetrieval",
            "hf_hub_name": "kornwtp/wangchanx-legalrag-tha-qaretrieval",
            "description": "The WangchanX-Legal-ThaiCCL-RAG dataset supports the development of legal question-answering systems in Thai using Retrieval-Augmented Generation (RAG).",
            "reference": "https://huggingface.co/datasets/airesearch/WangchanX-Legal-ThaiCCL-RAG",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["test"],
            "eval_langs": ["tha"],
            "main_score": "ndcg@k",
        }