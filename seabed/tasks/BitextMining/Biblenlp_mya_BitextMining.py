from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class Biblenlp_mya_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "Biblenlp_mya_BitextMining",
            "hf_hub_name": "kornwtp/biblenlp-mya-bitextmining",
            "description": "Parallel sentences in English and their corresponding sentences in Burmese.",
            "reference": "https://huggingface.co/datasets/bible-nlp/biblenlp-corpus",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["mya"],
            "main_score": "f1",
        }