from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class TagalogNTREX(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "TagalogNTREX",
            "hf_hub_name": "kornwtp/fil-ntrex",
            "description": "Parallel sentences in English and their corresponding sentences in Tagalog.",
            "reference": "https://huggingface.co/datasets/mteb/NTREX",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["tl"],
            "main_score": "mean_accuracy",
        }