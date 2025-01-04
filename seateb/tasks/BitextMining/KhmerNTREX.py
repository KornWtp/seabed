from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class KhmerNTREX(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "KhmerNTREX",
            "hf_hub_name": "kornwtp/km-ntrex",
            "description": "Parallel sentences in English and their corresponding sentences in Khmer.",
            "reference": "https://huggingface.co/datasets/mteb/IN22-Conv",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["km"],
            "main_score": "mean_accuracy",
        }