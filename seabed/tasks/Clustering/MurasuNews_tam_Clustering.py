from ...abstasks.AbsTaskClustering import AbsTaskClustering


class MurasuNews_tam_Clustering(AbsTaskClustering):
    @property
    def description(self):
        return {
            "name": "MurasuNews_tam_Clustering",
            "hf_hub_name": "kornwtp/murasu-news-tam-clustering",
            "description": "",
            "reference": "",
            "type": "Clustering",
            "category": "s2s",
            "eval_splits": ["train"],
            "eval_langs": ["tam"],
            "main_score": "v_measure",
        }