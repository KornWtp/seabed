from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class Biblenlp_tam_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "Biblenlp_tam_BitextMining",
            "hf_hub_name": "kornwtp/biblenlp-tam-bitextmining",
            "description": "Parallel sentences in English and their corresponding sentences in Tamil.",
            "reference": "https://huggingface.co/datasets/bible-nlp/biblenlp-corpus",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["tam"],
            "main_score": "f1",
        }