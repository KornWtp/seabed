from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class VietnameseBiblenlp(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "VietnameseBiblenlp",
            "hf_hub_name": "kornwtp/vi-biblenlp-corpus",
            "description": "Parallel sentences in English and their corresponding sentences in Vietnamese.",
            "reference": "https://huggingface.co/datasets/bible-nlp/biblenlp-corpus",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["vi"],
            "main_score": "mean_accuracy",
        }