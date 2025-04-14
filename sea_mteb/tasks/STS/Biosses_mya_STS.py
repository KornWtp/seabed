from ...abstasks.AbsTaskSTS import AbsTaskSTS


class Biosses_mya_STS(AbsTaskSTS):
    @property
    def description(self):
        return {
            "name": "Biosses_mya_STS",
            "hf_hub_name": "kornwtp/stsbiosses-mya-sts",
            "description": "Burmese Semantic Textual Similarity Benchmark (STSbenchmark) dataset.",
            "reference": "",
            "type": "STS",
            "category": "s2s",
            "eval_splits": ["train"],
            "eval_langs": ["mya"],
            "main_score": "cosine_spearman",
            "min_score": 0,
            "max_score": 5,
        }