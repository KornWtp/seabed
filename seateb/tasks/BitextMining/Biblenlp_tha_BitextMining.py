from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class Biblenlp_tha_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "Biblenlp_tha_BitextMining",
            "hf_hub_name": "kornwtp/biblenlp-tha-bitextmining",
            "description": "Parallel sentences in English and their corresponding sentences in Thai.",
            "reference": "https://huggingface.co/datasets/bible-nlp/biblenlp-corpus",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["tha"],
            "main_score": "f1",
        }