"""
LABEL MAPPER
------------
Maps ML model label outputs to human-readable response sentences
using a plain Python dictionary, as specified in the project context.

Example:
    Dataset column value = 3
    Dictionary entry: {"3": "Please provide a specific target date."}
"""
import random
from AIRE.vocab import BASIC_CONV, QUES, Vocab

DEFAULT_RESPONSE = "Thanks for the detail - could you elaborate a bit further?"


def map_label_to_response(label: str) -> str:
    """Look up the clarifying sentence for a given label."""
    print("LABEL(label_mapper) : ", label)
    if label in BASIC_CONV:
        return Vocab.get(str(label), DEFAULT_RESPONSE)
    elif label in QUES:
        return Vocab['question'].get(str(label), DEFAULT_RESPONSE)
