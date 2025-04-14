from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class QED_khm_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "QED_khm_BitextMining",
            "hf_hub_name": "kornwtp/qed-khm-bitextmining",
            "description": "Parallel sentences in English and their corresponding sentences in Khmer.",
            "reference": "https://opus.nlpl.eu",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["khm"],
            "main_score": "f1",
        }