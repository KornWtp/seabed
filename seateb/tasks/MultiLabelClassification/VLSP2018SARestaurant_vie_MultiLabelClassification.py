from ...abstasks.AbsTaskMultiLabelClassification import AbsTaskMultiLabelClassification


class VLSP2018SARestaurant_vie_MultiLabelClassification(AbsTaskMultiLabelClassification):
    @property
    def description(self):
        return {
            "name": "VLSP2018SARestaurant_vie_MultiLabelClassification",
            "hf_hub_name": "kornwtp/vlsp2018sa-restaurant-vie-multilabelclassification",
            "description": "Multilabel text sentiment analisis from Vietnamese restaurant reviews dataset..",
            "reference": "https://github.com/vndee/awsome-vietnamese-nlp",
            "category": "s2s",
            "type": "MultiLabelClassification",
            "eval_splits": ["test"],
            "eval_langs": ["vie"],
            "main_score": "f1",
        }