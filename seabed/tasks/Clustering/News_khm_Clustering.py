from ...abstasks.AbsTaskClustering import AbsTaskClustering


class News_khm_Clustering(AbsTaskClustering):
    @property
    def description(self):
        return {
            "name": "News_khm_Clustering",
            "hf_hub_name": "kornwtp/news-khm-clustering",
            "description": "",
            "reference": "",
            "type": "Clustering",
            "category": "s2s",
            "eval_splits": ["test"],
            "eval_langs": ["khm"],
            "main_score": "v_measure",
        }