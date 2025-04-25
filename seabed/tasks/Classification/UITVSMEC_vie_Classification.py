from ...abstasks.AbsTaskClassification import AbsTaskClassification


class UITVSMEC_vie_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "UITVSMEC_vie_Classification",
            "hf_hub_name": "kornwtp/uitvsmec-vie-classification",
            "description": "This dataset consists of Vietnamese Facebook comments that were manually annotated for sentiment.",
            "reference": "https://huggingface.co/datasets/SEACrowd/uit_vsmec",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["vie"],
            "main_score": "f1",
        }