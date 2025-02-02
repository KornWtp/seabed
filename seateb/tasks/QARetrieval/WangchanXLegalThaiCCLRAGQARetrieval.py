from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class WangchanXLegalThaiCCLRAGQARetrieval(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "WangchanXLegalThaiCCLRAGQARetrieval",
            "hf_hub_name": "kornwtp/WangchanX-Legal-ThaiCCL-RAG",
            "description": "The WangchanX-Legal-ThaiCCL-RAG dataset supports the development of legal question-answering systems in Thai using Retrieval-Augmented Generation (RAG).",
            "reference": "https://huggingface.co/datasets/airesearch/WangchanX-Legal-ThaiCCL-RAG",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["test"],
            "eval_langs": ["th"],
            "main_score": "ndcg@k",
        }