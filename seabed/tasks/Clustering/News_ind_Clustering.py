from ...abstasks.AbsTaskClustering import AbsTaskClustering


class News_ind_Clustering(AbsTaskClustering):
    @property
    def description(self):
        return {
            "name": "News_ind_Clustering",
            "hf_hub_name": "kornwtp/news-ind-clustering",
            "description": "",
            "reference": "",
            "type": "Clustering",
            "category": "s2s",
            "eval_splits": ["test"],
            "eval_langs": ["ind"],
            "main_score": "v_measure",
        }