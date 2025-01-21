from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class ThaiFlores(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "ThaiFloresBitextMining",
            "hf_hub_name": "kornwtp/th-flores",
            "description": "Parallel sentences in English and their corresponding sentences in Thai.",
            "reference": "https://huggingface.co/datasets/mteb/flores",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["devtest"],
            "eval_langs": ["th"],
            "main_score": "mean_accuracy",
        }