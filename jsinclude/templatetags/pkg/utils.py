def stripQuotes(string):
    """Strip leading and trailing quotes from a string.
    Does nothing unless starting and ending quotes are present and
    the same type (single or double).
    """
    single = string.startswith("'") and string.endswith("'")
    double = string.startswith('"') and string.endswith('"')
    if single or double:
        return string[1:-1]
    return string

def escapeQuotes(string):
    """Escape single quotes since values will be wrapped
    in single quotes in the wrap template.
    """
    try:
        return string.replace("'", "\\'")
    except AttributeError:
        # Not a string so return unaltered.
        return string

def fin(path):
    """Opens file at given path and returns string value.
    """
    return open(path, 'rb').read()
