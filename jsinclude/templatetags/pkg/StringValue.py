def StringValue(value):
    """StringValues are either JavaScript booleans or
    actual strings. JavaScript uses lower case booleans.
    """
    if value in ['true', 'false']:
        # Do not wrap JS booleans in quotes.
        return value
    else:
        # value is not a boolean, so wrap in quotes.
        return "'%s'" % value
