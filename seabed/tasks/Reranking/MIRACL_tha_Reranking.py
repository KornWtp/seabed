from ...abstasks.AbsTaskReranking import AbsTaskReranking


class MIRACL_tha_Reranking(AbsTaskReranking):
    @property
    def description(self):
        return {
            "name": "MIRACL_tha_Reranking",
            "hf_hub_name": "kornwtp/miracl_tha_reranking",
            "description": "Multilingual information retrieval across a continuum of languages.",
            "reference": "https://huggingface.co/datasets/miracl/miracl",
            "type": "Reranking",
            "category": "s2s",
            "eval_splits": ["dev"],
            "eval_langs": ["tha"],
            "main_score": "map",
        }