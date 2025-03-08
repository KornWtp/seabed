from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class Biblenlp_fil_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "Biblenlp_fil_BitextMining",
            "hf_hub_name": "kornwtp/biblenlp-fil-bitextmining",
            "description": "Parallel sentences in English and their corresponding sentences in Filipino.",
            "reference": "https://huggingface.co/datasets/bible-nlp/biblenlp-corpus",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["fil"],
            "main_score": "f1",
        }