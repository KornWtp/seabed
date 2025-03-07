from ...abstasks.AbsTaskClassification import AbsTaskClassification


class HSDNofaaulia_ind_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "HSDNofaaulia_ind_Classification",
            "hf_hub_name": "kornwtp/hsd-nofaaulia-ind-classification",
            "description": "Hate speech detection in Indonesian language",
            "reference": "https://huggingface.co/datasets/SEACrowd/id_hsd_nofaaulia",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["ind"],
            "main_score": "f1",
        }