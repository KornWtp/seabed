from ...abstasks.AbsTaskClassification import AbsTaskClassification


class JaDiIde_ind_Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "JaDiIde_ind_Classification",
            "hf_hub_name": "kornwtp/jadiide-ind-classification",
            "description": "The JaDi-Ide dataset is a Twitter dataset for Javanese dialect identification, containing 16,498 data samples. The dialect is classified into Standard Javanese, Ngapak Javanese, and East Javanese dialects.",
            "reference": "https://github.com/fathanick/Javanese-Dialect-Identification-from-Twitter-Data",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["ind"],
            "main_score": "f1",
        }