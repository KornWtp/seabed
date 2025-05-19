from ...abstasks.AbsTaskClustering import AbsTaskClustering


class News_mya_Clustering(AbsTaskClustering):
    @property
    def description(self):
        return {
            "name": "News_mya_Clustering",
            "hf_hub_name": "kornwtp/myanmarnews-mya-clustering",
            "description": "",
            "reference": "",
            "type": "Clustering",
            "category": "s2s",
            "eval_splits": ["train"],
            "eval_langs": ["mya"],
            "main_score": "v_measure",
        }