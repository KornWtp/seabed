from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class QED_zsm_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "QED_zsm_BitextMining",
            "hf_hub_name": "kornwtp/qed-zsm-bitextmining",
            "description": "Parallel sentences in English and their corresponding sentences in Malay.",
            "reference": "https://opus.nlpl.eu",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["zsm"],
            "main_score": "f1",
        }