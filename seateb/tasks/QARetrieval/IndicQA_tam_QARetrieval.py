from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class IndicQA_tam_QARetrieval(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "IndicQA_tam_QARetrieval",
            "hf_hub_name": "kornwtp/indicqa-tam-qaretrieval",
            "description": "The Indic QA dataset is designed for question answering tasks, with a focus on Tamil language.",
            "reference": "https://huggingface.co/datasets/ai4bharat/IndicQA",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["test"],
            "eval_langs": ["tam"],
            "main_score": "ndcg@k",
        }