"""
ML ENGINE (stub)
----------------
This is a placeholder for Model 1 (BA Brain) ambiguity/confidence scoring.
Replace classify_requirement() with a real scikit-learn pipeline
(e.g. TF-IDF + SVM or Naive Bayes) trained on your merged DataFrame.

Contract this function must honor (so app.py never needs to change):
    Input  : requirement_text (str)
    Output : {
        "confidence": float (0.0 - 1.0),
        "label": str (matches a key in label_mapper.LABEL_MAP)
    }
"""
import random
# Placeholder label set - replace with your real Label_BA_x / Label_QA_x etc.
DUMMY_LABELS = ["1", "2", "3", "4", "5"]


def classify_requirement(requirement_text: str) -> dict:
    """
    TEMPORARY STUB.
    Currently returns a random label + confidence so the
    Flask <-> UI <-> routing logic can be tested end-to-end
    before the real scikit-learn model is wired in.
    """
    confidence = round(random.uniform(0.60, 0.99), 2)
    # label = random.choice(DUMMY_LABELS)
    label = DUMMY_LABELS[0]

    return {
        "confidence": confidence,
        "label": label
    }
