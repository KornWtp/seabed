from ...abstasks.AbsTaskQARetrieval import AbsTaskQARetrieval


class ViQuAD2_0_vie_QARetrieval(AbsTaskQARetrieval):
    @property
    def description(self):
        return {
            "name": "ViQuAD2_0_vie_QARetrieval",
            "hf_hub_name": "kornwtp/viquad2.0-vie-qaretrieval",
            "description": "Vietnamese Question Answering dataset.",
            "reference": "https://huggingface.co/datasets/taidng/UIT-ViQuAD2.0",
            "category": "s2s",
            "type": "QARetrieval",
            "eval_splits": ["test"],
            "eval_langs": ["vie"],
            "main_score": "ndcg@k",
        }