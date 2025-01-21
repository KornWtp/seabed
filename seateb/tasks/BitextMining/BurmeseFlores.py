from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class BurmeseFloresBitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "BurmeseFloresBitextMining",
            "hf_hub_name": "kornwtp/my-flores",
            "description": "Parallel sentences in English and their corresponding sentences in Burmese.",
            "reference": "https://huggingface.co/datasets/mteb/flores",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["devtest"],
            "eval_langs": ["my"],
            "main_score": "f1",
        }