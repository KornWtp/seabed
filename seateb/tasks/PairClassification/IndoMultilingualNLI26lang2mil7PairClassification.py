from ...abstasks.AbsTaskPairClassification import AbsTaskPairClassification


class IndoMultilingualNLI26lang2mil7PairClassification(AbsTaskPairClassification):
    @property
    def description(self):
        return {
            "name": "IndoMultilingualNLI26lang2mil7PairClassification",
            "hf_hub_name": "kornwtp/id-multilingual-nli-26lang-2mil7",
            "description": "The dataset is based on the English datasets MultiNLI, Fever-NLI, ANLI, LingNLI and WANLI and was created using the latest open-source machine translation models.",
            "reference": "https://huggingface.co/datasets/MoritzLaurer/multilingual-NLI-26lang-2mil7",
            "category": "s2s",
            "type": "PairClassification",
            "eval_splits": ["id_anli"],
            "eval_langs": ["id"],
            "main_score": "ap",
        }