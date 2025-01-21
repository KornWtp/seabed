from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class ThaiTyDiQA(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "ThaiTyDiQAQARetrieval",
            "hf_hub_name": "kornwtp/th-tydiqa",
            "description": "Information-seeking question answering in typologically.",
            "reference": "https://huggingface.co/datasets/miracl/miracl",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["validation"],
            "eval_langs": ["th"],
            "main_score": "mrr",
        }