from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class IndoMIRACL(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "IndoMIRACL",
            "hf_hub_name": "kornwtp/id-miracl",
            "description": "Multilingual information retrieval across a continuum of languages.",
            "reference": "https://huggingface.co/datasets/miracl/miracl",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["dev"],
            "eval_langs": ["id"],
            "main_score": "mrr",
        }