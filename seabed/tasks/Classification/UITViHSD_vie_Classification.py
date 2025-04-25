from ...abstasks.AbsTaskClassification import AbsTaskClassification


class UITViHSD_vie_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "UITViHSD_vie_Classification",
            "hf_hub_name": "kornwtp/uitvihsd-vie-classification",
            "description": "The ViHSD dataset consists of comments collected from Facebook pages and YouTube channels that have a high-interactive rate, and do not restrict comments.",
            "reference": "https://github.com/sonlam1102/vihsd",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["vie"],
            "main_score": "f1",
        }