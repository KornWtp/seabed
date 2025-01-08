from ...abstasks.AbsTaskSTS import AbsTaskSTS


class TamilSTSBenchmarkSTS(AbsTaskSTS):
    @property
    def description(self):
        return {
            "name": "TamilSTSBenchmarkSTS",
            "hf_hub_name": "kornwtp/ta-stsbenchmark-sts",
            "description": "Tamil Semantic Textual Similarity Benchmark (STSbenchmark) dataset, translated from SentEval using the Google Translate API.",
            "reference": "http://ixa2.si.ehu.es/stswiki/index.php/STSbenchmark",
            "type": "STS",
            "category": "s2s",
            "eval_splits": ["test"],
            "eval_langs": ["tl"],
            "main_score": "cosine_spearman",
            "min_score": 0,
            "max_score": 5,
        }