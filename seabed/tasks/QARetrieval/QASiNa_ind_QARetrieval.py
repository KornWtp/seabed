from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class QASiNa_ind_QARetrieval(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "QASiNa_ind_QARetrieval",
            "hf_hub_name": "kornwtp/qasina-ind-qaretrieval",
            "description": "Question Answering Sirah Nabawiyah Dataset (QASiNa) is Extractive QA Dataset which build to perform QA task in Sirah Nabawiyah domain.",
            "reference": "https://github.com/rizquuula/QASiNa",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["train"],
            "eval_langs": ["ind"],
            "main_score": "ndcg@k",
        }