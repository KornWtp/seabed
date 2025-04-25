from ...abstasks.AbsTaskClassification import AbsTaskClassification


class UITVION_vie_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "UITVION_vie_Classification",
            "hf_hub_name": "kornwtp/uitvion-vie-classification",
            "description": "UIT-ViON (Vietnamese Online Newspaper) is a dataset collected from well-known online newspapers in Vietnamese.",
            "reference": "https://github.com/kh4nh12/UIT-ViON-Dataset",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["vie"],
            "main_score": "f1",
        }