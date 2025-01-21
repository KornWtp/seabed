from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class TamilTatoeba(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "TamilTatoebaBitextMining",
            "hf_hub_name": "kornwtp/ta-tatoeba",
            "description": "Parallel sentences in English and their corresponding sentences in Tamil.",
            "reference": "https://opus.nlpl.eu",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["ta"],
            "main_score": "mean_accuracy",
        }