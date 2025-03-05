from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class ACIQuAD_ind_QARetrieval(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "ACIQuAD_ind_QARetrieval",
            "hf_hub_name": "kornwtp/aciquad-ind-qaretrieval",
            "description": "This is an automatically-produced question answering datasetgenerated from Indonesian Wikipedia articles.",
            "reference": "https://huggingface.co/datasets/SEACrowd/ac_iquad",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["test"],
            "eval_langs": ["ind"],
            "main_score": "ndcg@k",
        }