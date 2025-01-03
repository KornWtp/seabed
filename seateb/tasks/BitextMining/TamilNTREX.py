from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class TamilNTREX(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "TamilNTREX",
            "hf_hub_name": "kornwtp/ta-ntrex",
            "description": "Parallel sentences in English and their corresponding sentences in Tamil.",
            "reference": "https://huggingface.co/datasets/mteb/NTREX",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["ta"],
            "main_score": "mean_accuracy",
        }