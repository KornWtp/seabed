from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class TyDiQA_tha_QARetrieval(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "TyDiQA_tha_QARetrieval",
            "hf_hub_name": "kornwtp/tydiqa-tha-qaretrieval",
            "description": "Information-seeking question answering in typologically.",
            "reference": "https://huggingface.co/datasets/miracl/miracl",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["validation"],
            "eval_langs": ["tha"],
            "main_score": "ndcg@k",
        }