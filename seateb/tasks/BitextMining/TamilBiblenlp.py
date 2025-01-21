from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class TamilBiblenlp(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "TamilBiblenlpBitextMining",
            "hf_hub_name": "kornwtp/ta-biblenlp-corpus",
            "description": "Parallel sentences in English and their corresponding sentences in Tamil.",
            "reference": "https://huggingface.co/datasets/bible-nlp/biblenlp-corpus",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["ta"],
            "main_score": "mean_accuracy",
        }