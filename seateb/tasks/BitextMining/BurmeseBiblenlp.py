from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class BurmeseBiblenlpBitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "BurmeseBiblenlpBitextMining",
            "hf_hub_name": "kornwtp/my-biblenlp-corpus",
            "description": "Parallel sentences in English and their corresponding sentences in Burmese.",
            "reference": "https://huggingface.co/datasets/bible-nlp/biblenlp-corpus",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["my"],
            "main_score": "f1",
        }