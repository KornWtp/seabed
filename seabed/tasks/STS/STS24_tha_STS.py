from ...abstasks.AbsTaskSTS import AbsTaskSTS


class STS24_tha_STS(AbsTaskSTS):
    @property
    def description(self):
        return {
            "name": "STS24_tha_STS",
            "hf_hub_name": "kornwtp/sts24-tha-sts",
            "description": "Thai Semantic Textual Similarity Benchmark (STSbenchmark) dataset.",
            "reference": "",
            "type": "STS",
            "category": "s2s",
            "eval_splits": ["test"],
            "eval_langs": ["tha"],
            "main_score": "cosine_spearman",
            "min_score": 0,
            "max_score": 5,
        }