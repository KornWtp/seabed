from ...abstasks.AbsTaskSTS import AbsTaskSTS


class TamilIndicCrosslingualSTS(AbsTaskSTS):
    @property
    def description(self):
        return {
            "name": "TamilIndicCrosslingualSTS",
            "hf_hub_name": "kornwtp/ta-indic-crosslingual-sts",
            "description": "Tamil Semantic Textual Similarity Benchmark (STSbenchmark) dataset.",
            "reference": "",
            "type": "STS",
            "category": "s2s",
            "eval_splits": ["test"],
            "eval_langs": ["ta"],
            "main_score": "cosine_spearman",
            "min_score": 0,
            "max_score": 5,
        }