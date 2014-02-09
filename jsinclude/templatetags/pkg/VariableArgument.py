from .utils import escapeQuotes

def VariableArgument(key, context):
    value = context[key]
    key = escapeQuotes(key)
    try:
        # Ensure only a single pair of wrapping quotes.
        value = escapeQuotes(value)
    except AttributeError:
        # Value is not a string, so do nothing.
        pass
    return {
        key: value
    }
