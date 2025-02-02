from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class WangchanXSyntheticInstructThai120kQARetrieval(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "WangchanXSyntheticInstructThai120kQARetrieval",
            "hf_hub_name": "kornwtp/wangchanx-seed-free-synthetic-instruct-thai-120k",
            "description": "This dataset contains about 120k synthetic instruction-following samples in Thai, generated using a novel seed-free approach.",
            "reference": "https://huggingface.co/datasets/airesearch/wangchanx-seed-free-synthetic-instruct-thai-120k",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["train"],
            "eval_langs": ["th"],
            "main_score": "ndcg@k",
        }