import logging

from tqdm import trange
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import precision_score, recall_score, f1_score
import numpy as np

from .Evaluator import Evaluator

logger = logging.getLogger(__name__)


class MultiLabelClassificationEvaluator(Evaluator):
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
        text_clf = OneVsRestClassifier(LinearSVC(class_weight='balanced', verbose=0))
        text_clf.fit(X_train_encode, self.y_train)
        test_predicted = text_clf.predict(X_test_encode)
        
        accuracy_per_label = np.mean(self.y_test == test_predicted, axis=0)
        label_frequencies = np.sum(self.y_test, axis=0)
        total_samples = self.y_test.shape[0]
        weights = label_frequencies / total_samples  # Frequency-based weights
        weighted_accuracy = np.sum(weights * accuracy_per_label) / np.sum(weights)

        precision = precision_score(self.y_test, test_predicted, average='weighted')
        recall = recall_score(self.y_test, test_predicted, average='weighted')
        f1 = f1_score(self.y_test, test_predicted, average='weighted')

        return {
            "accuracy": weighted_accuracy,
            "precision": precision,
            "recall": recall,
            "f1": f1,
        }
                