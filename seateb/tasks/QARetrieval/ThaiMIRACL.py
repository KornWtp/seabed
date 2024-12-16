from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class ThaiMIRACL(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "ThaiMIRACL",
            "hf_hub_name": "kornwtp/th-miracl",
            "description": "Multilingual information retrieval across a continuum of languages.",
            "reference": "https://huggingface.co/datasets/miracl/miracl",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["dev"],
            "eval_langs": ["th"],
            "main_score": "mrr",
        }