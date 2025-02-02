from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class IndoQAQARetrieval(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "IndoQAQARetrieval",
            "hf_hub_name": "kornwtp/indoqa",
            "description": "IndoQA is a monolingual question-answering dataset of Indonesian language (ind).",
            "reference": "https://huggingface.co/datasets/SEACrowd/indoqa",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["validation"],
            "eval_langs": ["id"],
            "main_score": "ndcg@k",
        }