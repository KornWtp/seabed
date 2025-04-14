from ...abstasks.AbsTaskSTS import AbsTaskSTS


class STSBenchmark_tha_STS(AbsTaskSTS):
    @property
    def description(self):
        return {
            "name": "STSBenchmark_tha_STS",
            "hf_hub_name": "kornwtp/stsbenchmark-tha-sts",
            "description": "Thai Semantic Textual Similarity Benchmark (STSbenchmark) dataset, translated from SentEval using the Google Translate API.",
            "reference": "http://ixa2.si.ehu.es/stswiki/index.php/STSbenchmark",
            "type": "STS",
            "category": "s2s",
            "eval_splits": ["test"],
            "eval_langs": ["tha"],
            "main_score": "cosine_spearman",
            "min_score": 0,
            "max_score": 5,
        }