from ...abstasks.AbsTaskSTS import AbsTaskSTS


class SemRel2024_ind_STS(AbsTaskSTS):
    @property
    def description(self):
        return {
            "name": "SemRel2024_ind_STS",
            "hf_hub_name": "kornwtp/semrel2024-ind-sts",
            "description": "Indonesian Semantic Textual Relatedness (STR) dataset.",
            "reference": "https://huggingface.co/datasets/SemRel/SemRel2024",
            "type": "STS",
            "category": "s2s",
            "eval_splits": ["test"],
            "eval_langs": ["ind"],
            "main_score": "cosine_spearman",
            "min_score": 0,
            "max_score": 1,
        }