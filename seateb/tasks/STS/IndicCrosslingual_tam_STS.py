from ...abstasks.AbsTaskSTS import AbsTaskSTS


class IndicCrosslingual_tam_STS(AbsTaskSTS):
    @property
    def description(self):
        return {
            "name": "IndicCrosslingual_tam_STS",
            "hf_hub_name": "kornwtp/indic-crosslingual-tam-sts",
            "description": "Tamil Semantic Textual Similarity Benchmark (STSbenchmark) dataset.",
            "reference": "",
            "type": "STS",
            "category": "s2s",
            "eval_splits": ["test"],
            "eval_langs": ["tam"],
            "main_score": "cosine_spearman",
            "min_score": 0,
            "max_score": 5,
        }