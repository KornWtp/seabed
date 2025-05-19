from ...abstasks.AbsTaskClustering import AbsTaskClustering


class News_lao_Clustering(AbsTaskClustering):
    @property
    def description(self):
        return {
            "name": "News_lao_Clustering",
            "hf_hub_name": "kornwtp/news-lao-clustering",
            "description": "",
            "reference": "",
            "type": "Clustering",
            "category": "s2s",
            "eval_splits": ["test"],
            "eval_langs": ["lao"],
            "main_score": "v_measure",
        }