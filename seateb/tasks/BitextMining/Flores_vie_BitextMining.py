from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class Flores_vie_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "Flores_vie_BitextMining",
            "hf_hub_name": "kornwtp/flores-vie-bitextmining",
            "description": "Parallel sentences in English and their corresponding sentences in Vitenamese.",
            "reference": "https://huggingface.co/datasets/mteb/flores",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["devtest"],
            "eval_langs": ["vie"],
            "main_score": "f1",
        }