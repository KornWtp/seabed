from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class TamilFlores(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "TamilFloresBitextMining",
            "hf_hub_name": "kornwtp/ta-flores",
            "description": "Parallel sentences in English and their corresponding sentences in Tamil.",
            "reference": "https://huggingface.co/datasets/mteb/flores",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["devtest"],
            "eval_langs": ["ta"],
            "main_score": "mean_accuracy",
        }