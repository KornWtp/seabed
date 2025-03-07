from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class AskCovidDrBot_mya_QARetrieval(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "AskCovidDrBot_mya_QARetrieval",
            "hf_hub_name": "kornwtp/askcovid-mya-qaretrieval",
            "description": "Burmese question and answer paired corpus",
            "reference": "https://github.com/ThuraAung1601/AskCovidDrBot",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["train"],
            "eval_langs": ["mya"],
            "main_score": "ndcg@k",
        }