from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class MalayChatGPTOpenQAQARetrieval(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "MalayChatGPTOpenQAQARetrieval",
            "hf_hub_name": "kornwtp/chatgpt-malaysian-open-qa",
            "description": "Synthetic Malaysian open QA generated using ChatGPT3.5 on MS Wikipedia, MS Common Crawl and Malaysia Hansard",
            "reference": "https://huggingface.co/datasets/mesolitica/chatgpt-malaysian-open-qa",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["train"],
            "eval_langs": ["ms"],
            "main_score": "ndcg@k",
        }