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
    string = string.replace('"', '\\"')
    string = string.replace("'", "\\'")
    return string
