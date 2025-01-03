from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class TamilIN22Conv(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "TamilIN22Conv",
            "hf_hub_name": "kornwtp/ta-IN22-Conv",
            "description": "Parallel sentences in English and their corresponding sentences in Tamil.",
            "reference": "https://huggingface.co/datasets/mteb/IN22-Conv",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["ta"],
            "main_score": "mean_accuracy",
        }