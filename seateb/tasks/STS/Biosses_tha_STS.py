from ...abstasks.AbsTaskSTS import AbsTaskSTS


class Biosses_tha_STS(AbsTaskSTS):
    @property
    def description(self):
        return {
            "name": "Biosses_tha_STS",
            "hf_hub_name": "kornwtp/stsbiosses-tha-sts",
            "description": "Thai Semantic Textual Similarity Benchmark (STSbenchmark) dataset.",
            "reference": "",
            "type": "STS",
            "category": "s2s",
            "eval_splits": ["train"],
            "eval_langs": ["tha"],
            "main_score": "cosine_spearman",
            "min_score": 0,
            "max_score": 5,
        }