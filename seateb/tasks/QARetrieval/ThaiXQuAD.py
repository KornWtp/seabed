from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class ThaiXQuAD(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "ThaiXQuAD",
            "hf_hub_name": "kornwtp/th-xquad",
            "description": "Cross-lingual question answering.",
            "reference": "https://huggingface.co/datasets/google/xquad",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["validation"],
            "eval_langs": ["th"],
            "main_score": "mrr",
        }