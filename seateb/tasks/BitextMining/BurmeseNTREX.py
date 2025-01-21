from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class BurmeseNTREXBitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "BurmeseNTREXBitextMining",
            "hf_hub_name": "kornwtp/my-ntrex",
            "description": "Parallel sentences in English and their corresponding sentences in Burmese.",
            "reference": "https://huggingface.co/datasets/mteb/NTREX",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["my"],
            "main_score": "f1",
        }