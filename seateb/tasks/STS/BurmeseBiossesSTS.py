from ...abstasks.AbsTaskSTS import AbsTaskSTS


class BurmeseBiossesSTS(AbsTaskSTS):
    @property
    def description(self):
        return {
            "name": "BurmeseBiossesSTS",
            "hf_hub_name": "kornwtp/my-stsbio-sts",
            "description": "Thai Semantic Textual Similarity Benchmark (STSbenchmark) dataset.",
            "reference": "",
            "type": "STS",
            "category": "s2s",
            "eval_splits": ["train"],
            "eval_langs": ["my"],
            "main_score": "cosine_spearman",
            "min_score": 0,
            "max_score": 5,
        }