from ...abstasks.AbsTaskTextClassification import AbsTaskTextClassification


class IndoJaDiIdeClassification(AbsTaskTextClassification):
    @property
    def description(self):
        return {
            "name": "IndoJaDiIdeClassification",
            "hf_hub_name": "kornwtp/id-jadi-ide-classification",
            "description": "The JaDi-Ide dataset is a Twitter dataset for Javanese dialect identification, containing 16,498 data samples. The dialect is classified into Standard Javanese, Ngapak Javanese, and East Javanese dialects.",
            "reference": "https://github.com/fathanick/Javanese-Dialect-Identification-from-Twitter-Data",
            "category": "s2s",
            "type": "TextClassification",
            "eval_splits": ["test"],
            "eval_langs": ["id"],
            "main_score": "f1",
        }