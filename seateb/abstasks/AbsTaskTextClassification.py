import logging

from sklearn.model_selection import train_test_split

from ..evaluation.evaluators import TextClassificationEvaluator
from .AbsTask import AbsTask


class AbsTaskTextClassification(AbsTask):
    """
    Abstract class for TextClassificationTasks
    
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def evaluate(self, model, split="test", **kwargs):
        if not self.data_loaded:
            self.load_data()
        
        data_split = self.dataset

        if "generated-reviews-enth" in self.description["hf_hub_name"]:
            X_train, y_train, X_test, y_test = self.generated_reviews_enth_preprocess(data_split)
        elif "ms-bahasa-twitter-sentiment" in self.description["hf_hub_name"]:
            X_train, y_train, X_test, y_test = self.generated_preprocess(data_split)
        elif "ms-news-sentiment" in self.description["hf_hub_name"]:
            X_train, y_train, X_test, y_test = self.generated_preprocess(data_split)
        elif "km-bookmebus-reviews" in self.description["hf_hub_name"]:
            X_train, y_train, X_test, y_test = self.generated_preprocess(data_split)
        elif "km-news-article-classification" in self.description["hf_hub_name"]:
            X_train, y_train, X_test, y_test = self.generated_preprocess(data_split)            
        else:
            X_train, y_train, X_test, y_test = self.preprocess(data_split)

        evaluator = TextClassificationEvaluator(
            X_train, y_train, X_test, y_test, **kwargs
        )
        scores = evaluator.compute_metrics(model)

        return scores

    def preprocess(self, data):
        X_train = data['train']['texts']
        y_train = data['train']['labels']
        
        X_test = data['test']['texts']
        y_test = data['test']['labels']

        return X_train, y_train, X_test, y_test

    def generated_preprocess(self, data):
        X_train = data['train']['texts']
        y_train = data['train']['labels']
        X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.20, random_state=42)

        return X_train, y_train, X_test, y_test

    def generated_reviews_enth_preprocess(self, data):
        X_train = [text['th'] for text in data['train']['texts']]
        y_train = data['train']['labels']
     
        X_test = [text['th'] for text in data['test']['texts']]
        y_test = data['test']['labels']
        
        return X_train, y_train, X_test, y_test

