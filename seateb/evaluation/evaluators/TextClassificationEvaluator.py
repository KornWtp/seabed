import logging

from tqdm import trange
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import precision_recall_fscore_support, accuracy_score
import numpy as np

from .Evaluator import Evaluator

logger = logging.getLogger(__name__)


class TextClassificationEvaluator(Evaluator):
    def __init__(
        self, X_train, y_train, X_test, y_test, batch_size=32, **kwargs
    ):
        super().__init__(**kwargs)
        self.X_train = X_train
        self.y_train = y_train
        self.X_test = X_test
        self.y_test = y_test
        self.batch_size = batch_size
        
        assert len(self.X_train) == len(self.y_train)
        assert len(self.X_test) == len(self.y_test)

    def __call__(self, model):
        scores = self.compute_metrics(model)

        return scores

    def compute_metrics(self, model):
        logger.info(f"Encoding {len(self.X_train)} sentences...")
        X_train_encode = model.encode(self.X_train, batch_size=self.batch_size)
        logger.info(f"Encoding {len(self.X_test)} sentences...")
        X_test_encode = model.encode(self.X_test, batch_size=self.batch_size)
        
        logger.info("Training classification head...") 
        text_clf = LinearSVC(class_weight='balanced', verbose=0)
        text_clf.fit(X_train_encode, self.y_train)
        test_predicted = text_clf.predict(X_test_encode)

        accuracy = accuracy_score(self.y_test, test_predicted)
        precision, recall, f1, _ = precision_recall_fscore_support(self.y_test, test_predicted, average="weighted")

        return {
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "f1": f1,
        }
                