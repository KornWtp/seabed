from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class TagalogBiblenlp(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "TagalogBiblenlpBitextMining",
            "hf_hub_name": "kornwtp/tl-biblenlp-corpus",
            "description": "Parallel sentences in English and their corresponding sentences in Tagalog.",
            "reference": "https://huggingface.co/datasets/bible-nlp/biblenlp-corpus",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["tl"],
            "main_score": "mean_accuracy",
        }