from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class BurmeseAskCovidDrBotQARetrieval(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "BurmeseAskCovidDrBotQARetrieval",
            "hf_hub_name": "kornwtp/burmese-covid-qa",
            "description": "Burmese question and answer paired corpus",
            "reference": "https://github.com/ThuraAung1601/AskCovidDrBot",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["train"],
            "eval_langs": ["my"],
            "main_score": "ndcg@k",
        }