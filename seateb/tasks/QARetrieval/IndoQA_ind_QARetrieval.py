from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class IndoQA_ind_QARetrieval(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "IndoQA_ind_QARetrieval",
            "hf_hub_name": "kornwtp/indoqa-ind-qaretrieval",
            "description": "IndoQA is a monolingual question-answering dataset of Indonesian language (ind).",
            "reference": "https://huggingface.co/datasets/SEACrowd/indoqa",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["validation"],
            "eval_langs": ["ind"],
            "main_score": "ndcg@k",
        }