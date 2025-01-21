from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class ThaiMLDR(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "ThaiMLDRQARetrieval",
            "hf_hub_name": "kornwtp/th-mldr",
            "description": "Thai document retrieval from Multilingual Long-Document Retrieval dataset.",
            "reference": "https://huggingface.co/datasets/Shitao/MLDR",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["test"],
            "eval_langs": ["th"],
            "main_score": "mrr",
        }