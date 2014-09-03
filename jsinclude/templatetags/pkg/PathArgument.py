from .utils import escapeQuotes
from .ArgumentValue import ArgumentValue

def PathArgument(context, path):
    """Resolve path from context variable is possible.
    """
    try:
        # Path argument was context variable name.
        return context[path]
    except KeyError:
        # Path argument was a string value.
        return path
