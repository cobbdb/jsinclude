from .utils import escapeQuotes

class VariableArgument(dict):
    def __new__(cls, key, context):
        value = context[key]
        value = escapeQuotes(value)
        key = escapeQuotes(key)
        return {
            key: value
        }
