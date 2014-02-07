from .utils import escapeQuotes, stripQuotes
from django.template import TemplateSyntaxError

class StaticArgument(dict):
    def __new__(cls, key):
        try:
            key = stripQuotes(key)
            key = escapeQuotes(key)
            tokens = key.split('=', 1)
            return {
                tokens[0]: tokens[1]
            }
        except IndexError:
            raise TemplateSyntaxError('JSInclude: Static data must be name=value or "name=long value".')
