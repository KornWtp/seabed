from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class TamilIndicQA(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "TamilIndicQA",
            "hf_hub_name": "kornwtp/ta-indicqa",
            "description": "The Indic QA dataset is designed for question answering tasks, with a focus on Tamil language.",
            "reference": "https://huggingface.co/datasets/ai4bharat/IndicQA",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["test"],
            "eval_langs": ["ta"],
            "main_score": "mrr",
        }