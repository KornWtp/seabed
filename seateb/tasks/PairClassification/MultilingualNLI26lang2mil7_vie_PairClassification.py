from ...abstasks.AbsTaskPairClassification import AbsTaskPairClassification


class MultilingualNLI26lang2mil7_vie_PairClassification(AbsTaskPairClassification):
    @property
    def description(self):
        return {
            "name": "MultilingualNLI26lang2mil7_vie_PairClassification",
            "hf_hub_name": "kornwtp/multilingual-nli-26lang-2mil7-vie-pairclassification",
            "description": "The dataset is based on the English datasets MultiNLI, Fever-NLI, ANLI, LingNLI and WANLI and was created using the latest open-source machine translation models.",
            "reference": "https://huggingface.co/datasets/MoritzLaurer/multilingual-NLI-26lang-2mil7",
            "category": "s2s",
            "type": "PairClassification",
            "eval_splits": ["vi_anli"],
            "eval_langs": ["vie"],
            "main_score": "ap",
        }