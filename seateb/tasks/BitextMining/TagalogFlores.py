from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class TagalogFlores(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "TagalogFloresBitextMining",
            "hf_hub_name": "kornwtp/tl-flores",
            "description": "Parallel sentences in English and their corresponding sentences in Tagalog.",
            "reference": "https://huggingface.co/datasets/mteb/flores",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["devtest"],
            "eval_langs": ["tl"],
            "main_score": "mean_accuracy",
        }