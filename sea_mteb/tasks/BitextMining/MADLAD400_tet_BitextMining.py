from ...abstasks.AbsTaskBitextMining import AbsTaskBitextMining


class MADLAD400_tet_BitextMining(AbsTaskBitextMining):
    @property
    def description(self):
        return {
            "name": "MADLAD400_tet_BitextMining",
            "hf_hub_name": "kornwtp/madlad400-tet-bitextmining",
            "description": "Parallel sentences in English and their corresponding sentences in Tetum.",
            "reference": "https://huggingface.co/datasets/raphaelmerx/MADLAD-400-Tetun",
            "category": "s2s",
            "type": "BitextMining",
            "eval_splits": ["train"],
            "eval_langs": ["tet"],
            "main_score": "f1",
        }