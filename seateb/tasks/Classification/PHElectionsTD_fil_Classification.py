from ...abstasks.AbsTaskClassification import AbsTaskClassification


class PHElectionsTD_fil_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "PHElectionsTD_fil_Classification",
            "hf_hub_name": "kornwtp/PHElectionsTD-fil-classificaiton",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["fil"],
            "main_score": "f1",
        }