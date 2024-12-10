from ...abstasks.AbsTaskSTS import AbsTaskSTS


class ThaiSTSBenchmarkSTS(AbsTaskSTS):
    @property
    def description(self):
        return {
            "name": "ThaiSTSBenchmark",
            "hf_hub_name": "kornwtp/th-stsbenchmark-sts",
            "description": "Thai Semantic Textual Similarity Benchmark (STSbenchmark) dataset.",
            "reference": "http://ixa2.si.ehu.es/stswiki/index.php/STSbenchmark",
            "type": "STS",
            "category": "s2s",
            "eval_splits": ["validation", "test"],
            "eval_langs": ["th"],
            "main_score": "cosine_spearman",
            "min_score": 0,
            "max_score": 5,
        }