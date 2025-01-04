from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class VietnameseFlores(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "VietnameseFlores",
            "hf_hub_name": "kornwtp/vi-flores",
            "description": "Parallel sentences in English and their corresponding sentences in Vitenamese.",
            "reference": "https://huggingface.co/datasets/mteb/flores",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["devtest"],
            "eval_langs": ["vi"],
            "main_score": "mean_accuracy",
        }