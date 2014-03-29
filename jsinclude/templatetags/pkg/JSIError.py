class JSIError(Exception):
    """JSIError wraps the message in html comments to be placed
    safely into the webpage.
    """
    def __init__(self, message, data={}):
        # Wrap the message in an html comment.
        message = "<!-- [JSInclude Error] %s %s -->" % (
            message,
            data.items()
        )
        Exception.__init__(self, message)
