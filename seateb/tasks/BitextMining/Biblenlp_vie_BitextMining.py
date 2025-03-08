from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class Biblenlp_vie_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "Biblenlp_vie_BitextMining",
            "hf_hub_name": "kornwtp/biblenlp-vie-bitextmining",
            "description": "Parallel sentences in English and their corresponding sentences in Vietnamese.",
            "reference": "https://huggingface.co/datasets/bible-nlp/biblenlp-corpus",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["vie"],
            "main_score": "f1",
        }