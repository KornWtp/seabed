from ...abstasks.AbsTaskSTS import AbsTaskSTS


class IndoSemRel2024STS(AbsTaskSTS):
    @property
    def description(self):
        return {
            "name": "IndoSemRel2024",
            "hf_hub_name": "kornwtp/id-SemRel2024",
            "description": "Indonesian Semantic Textual Relatedness (STR) dataset.",
            "reference": "https://huggingface.co/datasets/SemRel/SemRel2024",
            "type": "STS",
            "category": "s2s",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "cosine_spearman",
            "min_score": 0,
            "max_score": 1,
        }