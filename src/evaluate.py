"""Evaluation helpers for the phishing detection reproduction study."""
from __future__ import annotations

from typing import Any
import numpy as np
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    average_precision_score,
    balanced_accuracy_score,
    confusion_matrix,
    f1_score,
    fbeta_score,
    matthews_corrcoef,
    precision_score,
    recall_score,
    roc_auc_score,
)


def positive_probability(model: Any, X: pd.DataFrame) -> np.ndarray:
    """Return P(y=1) for a fitted binary classifier."""
    classes = list(model.classes_)
    if 1 not in classes:
        raise ValueError("The fitted model does not contain positive class 1.")
    return model.predict_proba(X)[:, classes.index(1)]


def evaluate_classifier(model: Any, X: pd.DataFrame, y: pd.Series) -> dict[str, float | int]:
    """Evaluate a fitted classifier with phishing as positive class 1."""
    prediction = model.predict(X)
    probability = positive_probability(model, X)
    tn, fp, fn, tp = confusion_matrix(y, prediction, labels=[0, 1]).ravel()
    return {
        "Accuracy": accuracy_score(y, prediction),
        "Balanced Accuracy": balanced_accuracy_score(y, prediction),
        "Precision": precision_score(y, prediction, zero_division=0),
        "Recall": recall_score(y, prediction, zero_division=0),
        "F1": f1_score(y, prediction, zero_division=0),
        "F2": fbeta_score(y, prediction, beta=2, zero_division=0),
        "MCC": matthews_corrcoef(y, prediction),
        "ROC-AUC": roc_auc_score(y, probability),
        "PR-AUC": average_precision_score(y, probability),
        "TN": int(tn),
        "FP": int(fp),
        "FN": int(fn),
        "TP": int(tp),
    }
