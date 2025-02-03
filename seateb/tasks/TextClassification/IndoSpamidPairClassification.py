from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class IndoSpamidPairClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "IndoSpamidPairClassification",
            "hf_hub_name": "kornwtp/id-spamid-pair-classification",
            "description": "SPAMID-PAIR is data post-comment pairs collected from 13 selected Indonesian public figures (artists) / public accounts with more than 15 million followers and categorized as famous artists.",
            "reference": "https://huggingface.co/datasets/SEACrowd/spamid_pair",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "f1",
        }