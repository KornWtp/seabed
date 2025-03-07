from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class Agricutlure1K_mya_QARetrieval(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "Agricutlure1K_mya_QARetrieval",
            "hf_hub_name": "kornwtp/agricutlure1k-mya-qaretrieval",
            "description": "Agriculture QA dataset in Burmese language",
            "reference": "https://huggingface.co/datasets/jojo-ai-mst/Myanmar-Agricutlure-1K",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["train"],
            "eval_langs": ["mya"],
            "main_score": "ndcg@k",
        }