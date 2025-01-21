from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class MyanmarAgricutlure1KQARetrieval(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "MyanmarAgricutlure1KQARetrieval",
            "hf_hub_name": "kornwtp/myanmar-agricutlure-1k",
            "description": "Agriculture QA dataset in Burmese language",
            "reference": "https://huggingface.co/datasets/jojo-ai-mst/Myanmar-Agricutlure-1K",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["train"],
            "eval_langs": ["my"],
            "main_score": "ndcg@k",
        }