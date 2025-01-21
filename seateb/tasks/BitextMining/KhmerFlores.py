from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class KhmerFlores(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "KhmerFloresBitextMining",
            "hf_hub_name": "kornwtp/km-flores",
            "description": "Parallel sentences in English and their corresponding sentences in Khmer.",
            "reference": "https://huggingface.co/datasets/mteb/flores",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["devtest"],
            "eval_langs": ["km"],
            "main_score": "mean_accuracy",
        }