import logging

from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.model_selection import train_test_split

from ..evaluation.evaluators import MultiLabelClassificationEvaluator
from .AbsTask import AbsTask


class AbsTaskMultiLabelClassification(AbsTask):
    """
    Abstract class for MultiLabelClassificationTasks
    
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def evaluate(self, model, prompts, split="test", **kwargs):
        if not self.data_loaded:
            self.load_data()
        
        data_split = self.dataset

        if "prachathai67k" in self.description["hf_hub_name"]:
            X_train, y_train, X_test, y_test = self.generated_prachathai67k_preprocess(data_split) 
        elif "vlsp2018sa" in self.description["hf_hub_name"]:
            X_train, y_train, X_test, y_test = self.vlsp2018sa_preprocess(data_split)       
        else:
            if "test" not in data_split.keys() and "validation" not in data_split.keys():
                X_train, y_train, X_test, y_test = self.generated_preprocess(data_split) 
            else:
                X_train, y_train, X_test, y_test = self.preprocess(data_split)

        if prompts is not None:
            X_train = prompts(self.description['type'], self.description['name'], X_train) 
            X_test = prompts(self.description['type'], self.description['name'], X_test)  
        
        evaluator = MultiLabelClassificationEvaluator(
            X_train, y_train, X_test, y_test, **kwargs
        )
        scores = evaluator.compute_metrics(model)

        return scores

    def preprocess(self, data):
        X_train = data['train']['texts']
        labels_train = data['train']['labels']
        
        try:
            X_test = data['test']['texts']
            labels_test = data['test']['labels']
        except:
            X_test = data['validation']['texts']
            labels_test = data['validation']['labels']

        mlb = MultiLabelBinarizer()
        y_train = mlb.fit_transform(labels_train)
        y_test = mlb.transform(labels_test)
        
        return X_train, y_train, X_test, y_test

    def generated_preprocess(self, data):
        X_train = data['train']['texts']
        labels = data['train']['labels']

        mlb = MultiLabelBinarizer()
        y_train = mlb.fit_transform(labels)
        X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.30, random_state=42)

        return X_train, y_train, X_test, y_test

    def generated_prachathai67k_preprocess(self, data):
        X_train = data['train']['body_text']
        labels = data['train']['labels']

        mlb = MultiLabelBinarizer()
        y_train = mlb.fit_transform(labels)
        X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.20, random_state=42)
        X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.10, random_state=42)

        return X_train, y_train, X_test, y_test

    def vlsp2018sa_preprocess(self, data):
        X_train = data['train']['review_text']
        labels_train = data['train']['all_sentiments']

        X_test = data['test']['review_text']
        labels_test = data['test']['all_sentiments']

        mlb = MultiLabelBinarizer()
        y_train = mlb.fit_transform(labels_train)
        y_test = mlb.transform(labels_test)

        return X_train, y_train, X_test, y_test
