from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class NTREX_vie_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "NTREX_vie_BitextMining",
            "hf_hub_name": "kornwtp/ntrex-vie-bitextmining",
            "description": "Parallel sentences in English and their corresponding sentences in Vitenamese.",
            "reference": "https://huggingface.co/datasets/mteb/NTREX",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["test"],
            "eval_langs": ["vie"],
            "main_score": "f1",
        }