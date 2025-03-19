from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class Microbiology1K_ind_QARetrieval(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "Microbiology1K_mya_QARetrieval",
            "hf_hub_name": "kornwtp/microbiology1k-mya-qaretrieval",
            "description": "Microbiology 1K QA pairs in Burmese Language",
            "reference": "https://huggingface.co/datasets/jojo-ai-mst/Burmese-Microbiology-1K",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["train"],
            "eval_langs": ["mya"],
            "main_score": "ndcg@k",
        }