from ...abstasks.AbsTaskClassification import AbsTaskClassification


class HateSpeech_ind_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "HateSpeech_ind_Classification",
            "hf_hub_name": "kornwtp/hatespeech-ind-classification",
            "description": "The ID Hatespeech dataset is collection of 713 tweets related to a political event, the Jakarta Governor Election 2017 designed for hate speech detection NLP task.",
            "reference": "https://huggingface.co/datasets/SEACrowd/id_hatespeech",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["ind"],
            "main_score": "f1",
        }