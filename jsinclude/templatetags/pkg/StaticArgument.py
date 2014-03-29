from .utils import escapeQuotes, stripQuotes
from .JSIError import JSIError
from .ArgumentValue import ArgumentValue

def StaticArgument(pair):
    """Tag argument as a dictionary by name: value. Static tag
    arguments must be of the form name=value or "name=long value".
    """
    try:
        pair = stripQuotes(pair)
        pair = escapeQuotes(pair)
        tokens = pair.split('=', 1)
        key = tokens[0]
        value = tokens[1]
    except IndexError:
        raise JSIError('Static argument must be name=value or "name=long value".', {
            'pair': pair
        })
    except:
        raise JSIError('Unknown error occured while parsing static argument.', {
            'pair': pair
        })

    return {
        key: ArgumentValue(value)
    }
