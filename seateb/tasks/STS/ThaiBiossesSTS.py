from ...abstasks.AbsTaskSTS import AbsTaskSTS


class ThaiBiossesSTS(AbsTaskSTS):
    @property
    def description(self):
        return {
            "name": "ThaiBiossesSTS",
            "hf_hub_name": "kornwtp/th-stsbio-sts",
            "description": "Thai Semantic Textual Similarity Benchmark (STSbenchmark) dataset.",
            "reference": "",
            "type": "STS",
            "category": "s2s",
            "eval_splits": ["train"],
            "eval_langs": ["th"],
            "main_score": "cosine_spearman",
            "min_score": 0,
            "max_score": 5,
        }