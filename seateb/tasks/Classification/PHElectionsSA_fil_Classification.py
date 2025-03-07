from ...abstasks.AbsTaskClassification import AbsTaskClassification


class PHElectionsSA_fil_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "PHElectionsSA_fil_Classification",
            "hf_hub_name": "kornwtp/PHElectionsSA-fil-classificaiton",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["fil"],
            "main_score": "f1",
        }