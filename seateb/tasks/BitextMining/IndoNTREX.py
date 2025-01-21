from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class IndoNTREX(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "IndoNTREXBitextMining",
            "hf_hub_name": "kornwtp/id-ntrex",
            "description": "Parallel sentences in English and their corresponding sentences in Indonesian.",
            "reference": "https://huggingface.co/datasets/mteb/NTREX",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "mean_accuracy",
        }