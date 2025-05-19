from ...abstasks.AbsTaskClustering import AbsTaskClustering


class News_tam_Clustering(AbsTaskClustering):
    @property
    def description(self):
        return {
            "name": "News_tam_Clustering",
            "hf_hub_name": "kornwtp/news-tam-clustering",
            "description": "",
            "reference": "",
            "type": "Clustering",
            "category": "s2s",
            "eval_splits": ["validation"],
            "eval_langs": ["tam"],
            "main_score": "v_measure",
        }