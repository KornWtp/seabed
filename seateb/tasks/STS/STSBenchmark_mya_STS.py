from ...abstasks.AbsTaskSTS import AbsTaskSTS


class STSBenchmark_mya_STS(AbsTaskSTS):
    @property
    def description(self):
        return {
            "name": "STSBenchmark_mya_STS",
            "hf_hub_name": "kornwtp/stsbenchmark-mya-sts",
            "description": "Burmese Semantic Textual Similarity Benchmark (STSbenchmark) dataset, translated from SentEval using the Google Translate API.",
            "reference": "http://ixa2.si.ehu.es/stswiki/index.php/STSbenchmark",
            "type": "STS",
            "category": "s2s",
            "eval_splits": ["test"],
            "eval_langs": ["mya"],
            "main_score": "cosine_spearman",
            "min_score": 0,
            "max_score": 5,
        }