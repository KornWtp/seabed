from ...abstasks.AbsTaskClassification import AbsTaskClassification


class PhoATIS_vie_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "PhoATIS_vie_Classification",
            "hf_hub_name": "kornwtp/phoatis-vie-classification",
            "description": "This corpus is intent detection and slot filling dataset for Vietnamese.",
            "reference": "https://github.com/VinAIResearch/JointIDSF/",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["vie"],
            "main_score": "f1",
        }