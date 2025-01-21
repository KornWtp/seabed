from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class ThaiNTREX(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "ThaiNTREXBitextMining",
            "hf_hub_name": "kornwtp/th-ntrex",
            "description": "Parallel sentences in English and their corresponding sentences in Thai.",
            "reference": "https://huggingface.co/datasets/mteb/NTREX",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["th"],
            "main_score": "mean_accuracy",
        }