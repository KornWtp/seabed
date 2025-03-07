from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class MIRACL_ind_QARetrieval(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "MIRACL_ind_QARetrieval",
            "hf_hub_name": "kornwtp/miracl-ind-qaretrieval",
            "description": "Multilingual information retrieval across a continuum of languages.",
            "reference": "https://huggingface.co/datasets/miracl/miracl",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["dev"],
            "eval_langs": ["ind"],
            "main_score": "ndcg@k",
        }