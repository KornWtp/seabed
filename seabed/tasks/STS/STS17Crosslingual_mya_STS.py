from ...abstasks.AbsTaskSTS import AbsTaskSTS


class STS17Crosslingual_mya_STS(AbsTaskSTS):
    @property
    def description(self):
        return {
            "name": "STS17Crosslingual_mya_STS",
            "hf_hub_name": "kornwtp/sts17-crosslingual-mya-sts",
            "description": "Burmese Semantic Textual Similarity Benchmark (STSbenchmark) dataset.",
            "reference": "",
            "type": "STS",
            "category": "s2s",
            "eval_splits": ["test"],
            "eval_langs": ["mya"],
            "main_score": "cosine_spearman",
            "min_score": 0,
            "max_score": 5,
        }