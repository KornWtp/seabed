from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class ChatGPTOpenQA_zsm_QARetrieval(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "ChatGPTOpenQA_zsm_QARetrieval",
            "hf_hub_name": "kornwtp/chatgpt-openqa-zsm-qaretrieval",
            "description": "Synthetic Malaysian open QA generated using ChatGPT3.5 on MS Wikipedia, MS Common Crawl and Malaysia Hansard",
            "reference": "https://huggingface.co/datasets/mesolitica/chatgpt-malaysian-open-qa",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["train"],
            "eval_langs": ["zsm"],
            "main_score": "ndcg@k",
        }