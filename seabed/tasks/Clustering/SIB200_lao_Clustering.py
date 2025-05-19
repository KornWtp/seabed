from ...abstasks.AbsTaskClustering import AbsTaskClustering


class SIB200_lao_Clustering(AbsTaskClustering):
    @property
    def description(self):
        return {
            "name": "SIB200_lao_Clustering",
            "hf_hub_name": "kornwtp/sib200-lao-clustering",
            "description": "SIB-200 is the largest publicly available topic classification dataset based on Flores-200 covering 205 languages and dialects.",
            "reference": "https://github.com/dadelani/sib-200",
            "type": "Clustering",
            "category": "s2s",
            "eval_splits": ["test"],
            "eval_langs": ["lao"],
            "main_score": "v_measure",
        }