from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class IN22Conv_tam_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "IN22Conv_tam_BitextMining",
            "hf_hub_name": "kornwtp/in22conv-tam-bitextmining",
            "description": "Parallel sentences in English and their corresponding sentences in Tamil.",
            "reference": "https://huggingface.co/datasets/mteb/IN22-Conv",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["tam"],
            "main_score": "f1",
        }