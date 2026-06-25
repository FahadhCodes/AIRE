"""
LABEL MAPPER
------------
Maps ML model label outputs to human-readable response sentences
using a plain Python dictionary, as specified in the project context.

Example:
    Dataset column value = 3
    Dictionary entry: {"3": "Please provide a specific target date."}
"""

LABEL_MAP = {
    "1": "Could you clarify which user role performs this action?",
    "2": "What should happen if this action fails?",
    "3": "Please provide a specific target date.",
    "4": "Can you specify the expected response time for this feature?",
    "5": "Should this requirement apply to all user roles or a specific one?",
}

DEFAULT_RESPONSE = "Thanks for the detail - could you elaborate a bit further?"


def map_label_to_response(label: str) -> str:
    """Look up the clarifying sentence for a given label."""
    return LABEL_MAP.get(str(label), DEFAULT_RESPONSE)
