from ...abstasks.AbsTaskClassification import AbsTaskClassification


class UITViCTSD_vie_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "UITViCTSD_vie_Classification",
            "hf_hub_name": "kornwtp/uitvictsd-vie-classification",
            "description": "The UIT-ViCTSD (Vietnamese Constructive and Toxic Speech Detection dataset) is a compilation of 10,000 human-annotated comments intended for constructive and toxic comments detection.",
            "reference": "https://github.com/tarudesu/ViCTSD",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["vie"],
            "main_score": "f1",
        }