from .StringValue import StringValue

def ArgumentValue(value):
    """Numbers and JS Booleans are not wrapped in quotes.
    Only actual strings are wrapped.
    """
    try:
        # True if string value is a Number (int or float).
        float(value)
        return value
    except ValueError:
        # value is not a Number, so return as StringValue.
        return StringValue(value)
