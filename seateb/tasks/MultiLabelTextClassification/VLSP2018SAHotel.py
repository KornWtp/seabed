from ...abstasks.AbsTaskMultiLabelTextClassification import AbsTaskMultiLabelTextClassification


class VLSP2018SAHotel(AbsTaskMultiLabelTextClassification):
    @property
    def description(self):
        return {
            "name": "VLSP2018SAHotelMultiLabelTextClassification",
            "hf_hub_name": "kornwtp/VLSP2018-SA-Hotel",
            "description": "Multilabel text sentiment analisis from Vietnamese hotel reviews dataset.",
            "reference": "https://github.com/vndee/awsome-vietnamese-nlp",
            "category": "s2s",
            "type": "MultiLabelTextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["vi"],
            "main_score": "f1",
        }