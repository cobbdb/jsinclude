from .utils import escapeQuotes

class VariableArgument(dict):
    def __new__(cls, key, context):
        try:
            value = context[key]
            value = escapeQuotes(value)
            key = escapeQuotes(key)
        except AttributeError:
            key = escapeQuotes(key)
        return {
            key: value
        }
