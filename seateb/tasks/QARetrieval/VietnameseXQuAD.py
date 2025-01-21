from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class VietnameseXQuAD(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "VietnameseXQuADQARetrieval",
            "hf_hub_name": "kornwtp/vi-xquad",
            "description": "Cross-lingual question answering.",
            "reference": "https://huggingface.co/datasets/google/xquad",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["validation"],
            "eval_langs": ["vi"],
            "main_score": "mrr",
        }