from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class VietnameseNTREX(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "VietnameseNTREXBitextMining",
            "hf_hub_name": "kornwtp/vi-ntrex",
            "description": "Parallel sentences in English and their corresponding sentences in Vitenamese.",
            "reference": "https://huggingface.co/datasets/mteb/NTREX",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["vi"],
            "main_score": "mean_accuracy",
        }