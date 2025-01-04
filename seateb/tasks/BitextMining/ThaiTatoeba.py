from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class ThaiTatoeba(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "ThaiTatoeba",
            "hf_hub_name": "kornwtp/th-tatoeba",
            "description": "Parallel sentences in English and their corresponding sentences in Thai.",
            "reference": "https://opus.nlpl.eu",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["th"],
            "main_score": "mean_accuracy",
        }