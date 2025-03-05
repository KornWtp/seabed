from ...abstasks.AbsTaskMultiLabelClassification import AbsTaskMultiLabelClassification


class VLSP2018SAHotel_vie_MultiLabelClassification(AbsTaskMultiLabelClassification):
    @property
    def description(self):
        return {
            "name": "VLSP2018SAHotel_vie_MultiLabelClassification",
            "hf_hub_name": "kornwtp/vlsp2018sa-hotel-vie-multilabelclassification",
            "description": "Multilabel text sentiment analisis from Vietnamese hotel reviews dataset.",
            "reference": "https://github.com/vndee/awsome-vietnamese-nlp",
            "category": "s2s",
            "type": "MultiLabelClassification",
            "eval_splits": ["test"],
            "eval_langs": ["vie"],
            "main_score": "f1",
        }