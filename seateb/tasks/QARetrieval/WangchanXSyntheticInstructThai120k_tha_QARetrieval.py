from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class WangchanXSyntheticInstructThai120k_tha_QARetrieval(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "WangchanXSyntheticInstructThai120k_tha_QARetrieval",
            "hf_hub_name": "kornwtp/wangchanx-synthetic-instruct120k-tha-qaretrieval",
            "description": "This dataset contains about 120k synthetic instruction-following samples in Thai, generated using a novel seed-free approach.",
            "reference": "https://huggingface.co/datasets/airesearch/wangchanx-seed-free-synthetic-instruct-thai-120k",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["train"],
            "eval_langs": ["tha"],
            "main_score": "ndcg@k",
        }