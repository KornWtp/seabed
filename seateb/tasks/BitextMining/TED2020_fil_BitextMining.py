from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class TED2020_fil_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "TED2020_fil_BitextMining",
            "hf_hub_name": "kornwtp/ted2020-fil-bitextmining",
            "description": "Parallel sentences in English and their corresponding sentences in Filipino.",
            "reference": "https://opus.nlpl.eu",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["fil"],
            "main_score": "f1",
        }