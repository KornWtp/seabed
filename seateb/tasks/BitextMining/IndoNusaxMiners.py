from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class IndoNusaxMiners(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "IndoNusaxMiners",
            "hf_hub_name": "kornwtp/id-nusax-miners",
            "description": "Parallel sentences in English and their corresponding sentences in Indonesian.",
            "reference": "https://huggingface.co/datasets/gentaiscool/bitext_nusax_miners",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["id"],
            "main_score": "mean_accuracy",
        }