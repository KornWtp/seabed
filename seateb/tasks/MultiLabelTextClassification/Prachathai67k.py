from ...abstasks.AbsTaskMultiLabelTextClassification import AbsTaskMultiLabelTextClassification


class Prachathai67k(AbsTaskMultiLabelTextClassification):
    @property
    def description(self):
        return {
            "name": "Prachathai67k",
            "hf_hub_name": "kornwtp/prachathai-67k",
            "description": "Thai multilabel text classification using the News Article Corpus from Prachathai.com.",
            "reference": "https://github.com/PyThaiNLP/prachathai-67k",
            "category": "s2s",
            "type": "MultiLabelTextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["th"],
            "main_score": "f1",
        }