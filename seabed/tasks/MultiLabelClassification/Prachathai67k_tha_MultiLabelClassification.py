from ...abstasks.AbsTaskMultiLabelClassification import AbsTaskMultiLabelClassification


class Prachathai67k_tha_MultiLabelClassification(AbsTaskMultiLabelClassification):
    @property
    def description(self):
        return {
            "name": "Prachathai67k_tha_MultiLabelClassification",
            "hf_hub_name": "kornwtp/prachathai67k-tha-multilabelclassification",
            "description": "Thai multilabel text classification using the News Article Corpus from Prachathai.com.",
            "reference": "https://github.com/PyThaiNLP/prachathai-67k",
            "category": "s2s",
            "type": "MultiLabelClassification",
            "eval_splits": ["test"],
            "eval_langs": ["tha"],
            "main_score": "f1",
        }