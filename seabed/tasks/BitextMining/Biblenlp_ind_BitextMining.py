from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class Biblenlp_ind_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "Biblenlp_ind_BitextMining",
            "hf_hub_name": "kornwtp/biblenlp-ind-bitextmining",
            "description": "Parallel sentences in English and their corresponding sentences in Indonesian.",
            "reference": "https://huggingface.co/datasets/bible-nlp/biblenlp-corpus",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["ind"],
            "main_score": "f1",
        }