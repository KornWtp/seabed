from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class QED_fil_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "QED_fil_BitextMining",
            "hf_hub_name": "kornwtp/qed_fil_bitextmining",
            "description": "Parallel sentences in English and their corresponding sentences in Filipino.",
            "reference": "https://opus.nlpl.eu",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["fil"],
            "main_score": "f1",
        }