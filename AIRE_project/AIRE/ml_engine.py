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
from AIRE.vocab import BASIC_CONV, QUES, DUMMY_LABELS, greets
import json
import spacy


nlp = spacy.load('en_core_web_md')


def classify_requirement(requirement_text: str) -> dict:
    """
    TEMPORARY STUB.
    Currently returns a random label + confidence so the
    Flask <-> UI <-> routing logic can be tested end-to-end
    before the real scikit-learn model is wired in.
    """
    confidence = round(random.uniform(0.60, 0.99), 2)
    label = random.choice(DUMMY_LABELS)
    doc = nlp(requirement_text)
    if len(doc) < 5 and True in [greet.lower() in [x.text.lower() for x in doc] for greet in greets]:
        label = random.choice(BASIC_CONV)
        confidence = 0.9
    print("DEBUGGING|||||||||:", label, confidence)
    return {
        "confidence": confidence,
        "label": label
    }
