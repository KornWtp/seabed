from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class QED_tam_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "QED_tam_BitextMining",
            "hf_hub_name": "kornwtp/qed-tam-bitextmining",
            "description": "Parallel sentences in English and their corresponding sentences in Tamil.",
            "reference": "https://opus.nlpl.eu",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["tam"],
            "main_score": "f1",
        }