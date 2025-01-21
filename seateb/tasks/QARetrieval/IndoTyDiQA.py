from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class IndoTyDiQA(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "IndoTyDiQAQARetrieval",
            "hf_hub_name": "kornwtp/id-tydiqa",
            "description": "Information-seeking question answering in typologically.",
            "reference": "https://huggingface.co/datasets/miracl/miracl",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["validation"],
            "eval_langs": ["id"],
            "main_score": "mrr",
        }