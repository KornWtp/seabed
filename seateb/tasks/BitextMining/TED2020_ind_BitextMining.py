from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class TED2020_ind_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "TED2020_ind_BitextMining",
            "hf_hub_name": "kornwtp/ted2020-ind-bitextmininig",
            "description": "Parallel sentences in English and their corresponding sentences in Indonesian.",
            "reference": "https://opus.nlpl.eu",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["ind"],
            "main_score": "f1",
        }