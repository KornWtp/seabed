from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class LaoFloresBitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "LaoFloresBitextMining",
            "hf_hub_name": "kornwtp/lo-flores",
            "description": "Parallel sentences in English and their corresponding sentences in Lao.",
            "reference": "https://huggingface.co/datasets/mteb/flores",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["devtest"],
            "eval_langs": ["lo"],
            "main_score": "mean_accuracy",
        }