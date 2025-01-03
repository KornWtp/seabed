from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class IndoBiblenlp(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "IndoBiblenlp",
            "hf_hub_name": "kornwtp/id-biblenlp-corpus",
            "description": "Parallel sentences in English and their corresponding sentences in Indonesian.",
            "reference": "https://huggingface.co/datasets/bible-nlp/biblenlp-corpus",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "mean_accuracy",
        }