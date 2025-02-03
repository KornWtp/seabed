from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class IndoHSDNofaauliaClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "IndoHSDNofaauliaClassification",
            "hf_hub_name": "kornwtp/id-hsd-nofaaulia-classification",
            "description": "Hate speech detection in Indonesian language",
            "reference": "https://huggingface.co/datasets/SEACrowd/id_hsd_nofaaulia",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "f1",
        }