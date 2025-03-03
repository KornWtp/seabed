from ...abstasks.AbsTaskSTS import AbsTaskSTS


class ThaiSTS22STS(AbsTaskSTS):
    @property
    def description(self):
        return {
            "name": "ThaiSTS22STS",
            "hf_hub_name": "kornwtp/th-sts22-sts",
            "description": "Thai Semantic Textual Similarity Benchmark (STSbenchmark) dataset.",
            "reference": "",
            "type": "STS",
            "category": "s2s",
            "eval_splits": ["test"],
            "eval_langs": ["th"],
            "main_score": "cosine_spearman",
            "min_score": 0,
            "max_score": 5,
        }