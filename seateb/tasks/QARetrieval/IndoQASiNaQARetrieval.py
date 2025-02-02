from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class IndoQASiNaQARetrieval(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "IndoQASiNaQARetrieval",
            "hf_hub_name": "kornwtp/id-qasina",
            "description": "Question Answering Sirah Nabawiyah Dataset (QASiNa) is Extractive QA Dataset which build to perform QA task in Sirah Nabawiyah domain.",
            "reference": "https://github.com/rizquuula/QASiNa",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["train"],
            "eval_langs": ["id"],
            "main_score": "ndcg@k",
        }