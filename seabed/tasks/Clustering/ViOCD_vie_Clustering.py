from ...abstasks.AbsTaskClustering import AbsTaskClustering


class ViOCD_vie_Clustering(AbsTaskClustering):
    @property
    def description(self):
        return {
            "name": "ViOCD_vie_Clustering",
            "hf_hub_name": "kornwtp/viocd-vie-clustering",
            "description": "",
            "reference": "",
            "type": "Clustering",
            "category": "s2s",
            "eval_splits": ["test"],
            "eval_langs": ["vie"],
            "main_score": "v_measure",
        }