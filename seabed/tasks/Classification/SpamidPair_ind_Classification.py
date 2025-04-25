from ...abstasks.AbsTaskClassification import AbsTaskClassification


class SpamidPair_ind_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "SpamidPair_ind_Classification",
            "hf_hub_name": "kornwtp/spamid-pair-ind-classification",
            "description": "SPAMID-PAIR is data post-comment pairs collected from 13 selected Indonesian public figures (artists) / public accounts with more than 15 million followers and categorized as famous artists.",
            "reference": "https://huggingface.co/datasets/SEACrowd/spamid_pair",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["ind"],
            "main_score": "f1",
        }