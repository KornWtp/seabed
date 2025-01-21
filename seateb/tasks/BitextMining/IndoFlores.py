from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class IndoFlores(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "IndoFloresBitextMining",
            "hf_hub_name": "kornwtp/id-flores",
            "description": "Parallel sentences in English and their corresponding sentences in Indonesian.",
            "reference": "https://huggingface.co/datasets/mteb/flores",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["devtest"],
            "eval_langs": ["id"],
            "main_score": "mean_accuracy",
        }