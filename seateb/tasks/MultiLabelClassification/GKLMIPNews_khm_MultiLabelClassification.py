from ...abstasks.AbsTaskMultiLabelClassification import AbsTaskMultiLabelClassification


class GKLMIPNews_khm_MultiLabelClassification(AbsTaskMultiLabelClassification):
    @property
    def description(self):
        return {
            "name": "GKLMIPNews_khm_MultiLabelClassification",
            "hf_hub_name": "kornwtp/gklmip-news-khm-multilabelclassification",
            "description": "The GKLMIP Khmer News Dataset is scraped from the Voice of America Khmer website.",
            "reference": "https://github.com/GKLMIP/Pretrained-Models-For-Khmer",
            "category": "s2s",
            "type": "MultiLabelClassification",
            "eval_splits": ["test"],
            "eval_langs": ["khm"],
            "main_score": "f1",
        }