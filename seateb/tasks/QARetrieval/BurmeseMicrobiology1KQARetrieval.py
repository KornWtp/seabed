from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class BurmeseMicrobiology1KQARetrieval(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "BurmeseMicrobiology1KQARetrieval",
            "hf_hub_name": "kornwtp/burmese-microbiology-1k",
            "description": "Microbiology 1K QA pairs in Burmese Language",
            "reference": "https://huggingface.co/datasets/jojo-ai-mst/Burmese-Microbiology-1K",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["train"],
            "eval_langs": ["my"],
            "main_score": "ndcg@k",
        }