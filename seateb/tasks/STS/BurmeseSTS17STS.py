from ...abstasks.AbsTaskSTS import AbsTaskSTS


class BurmeseSTS17STS(AbsTaskSTS):
    @property
    def description(self):
        return {
            "name": "BurmeseSTS17STS",
            "hf_hub_name": "kornwtp/my-sts17-sts",
            "description": "Thai Semantic Textual Similarity Benchmark (STSbenchmark) dataset.",
            "reference": "",
            "type": "STS",
            "category": "s2s",
            "eval_splits": ["test"],
            "eval_langs": ["my"],
            "main_score": "cosine_spearman",
            "min_score": 0,
            "max_score": 5,
        }