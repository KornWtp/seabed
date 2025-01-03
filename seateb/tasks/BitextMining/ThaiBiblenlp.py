from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class ThaiBiblenlp(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "ThaiBiblenlp",
            "hf_hub_name": "kornwtp/th-biblenlp-corpus",
            "description": "Parallel sentences in English and their corresponding sentences in Thai.",
            "reference": "https://huggingface.co/datasets/bible-nlp/biblenlp-corpus",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["th"],
            "main_score": "mean_accuracy",
        }