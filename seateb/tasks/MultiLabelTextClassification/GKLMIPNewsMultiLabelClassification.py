from ...abstasks.AbsTaskMultiLabelTextClassification import AbsTaskMultiLabelTextClassification


class GKLMIPNewsMultiLabelClassification(AbsTaskMultiLabelTextClassification):
    @property
    def description(self):
        return {
            "name": "GKLMIPNewsMultiLabelClassification",
            "hf_hub_name": "kornwtp/gklmip-newsclass-multilabel-classification",
            "description": "The GKLMIP Khmer News Dataset is scraped from the Voice of America Khmer website.",
            "reference": "https://github.com/GKLMIP/Pretrained-Models-For-Khmer",
            "category": "s2s",
            "type": "MultiLabelTextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["km"],
            "main_score": "f1",
        }