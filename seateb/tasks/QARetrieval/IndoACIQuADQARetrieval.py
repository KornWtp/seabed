from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class IndoACIQuADQARetrieval(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "IndoACIQuADQARetrieval",
            "hf_hub_name": "kornwtp/id-ac-iquad",
            "description": "This is an automatically-produced question answering datasetgenerated from Indonesian Wikipedia articles.",
            "reference": "https://huggingface.co/datasets/SEACrowd/ac_iquad",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "ndcg@k",
        }