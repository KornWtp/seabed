from ...abstasks.AbsTaskClustering import AbsTaskClustering


class EMoTES3K_fil_Clustering(AbsTaskClustering):
    @property
    def description(self):
        return {
            "name": "EMoTES3K_fil_Clustering",
            "hf_hub_name": "kornwtp/emotes3k-fil-clustering",
            "description": "",
            "reference": "",
            "type": "Clustering",
            "category": "s2s",
            "eval_splits": ["test"],
            "eval_langs": ["fil"],
            "main_score": "v_measure",
        }