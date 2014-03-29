from .utils import escapeQuotes
from .ArgumentValue import ArgumentValue

def VariableArgument(key, context):
    """Template context variable as a dictionary.
    """
    value = context[key]

    # Ensure only a single pair of wrapping quotes.
    key = escapeQuotes(key)
    value = escapeQuotes(value)

    return {
        key: ArgumentValue(value)
    }
