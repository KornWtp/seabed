from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class TyDiQA_ind_QARetrieval(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "TyDiQA_ind_QARetrieval",
            "hf_hub_name": "kornwtp/tydiqa-ind-qaretrieval",
            "description": "Information-seeking question answering in typologically.",
            "reference": "https://huggingface.co/datasets/miracl/miracl",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["validation"],
            "eval_langs": ["ind"],
            "main_score": "ndcg@k",
        }