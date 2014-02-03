from jsincludenode import JSIncludeNode
from django.template import TemplateSyntaxError, Library
register = Library()

@register.tag
def jsinclude(parser, token):
    # Separate all tag arguments.
    contents = token.split_contents()

    # Grab path to script.
    try:
        path = contents[1]
    except IndexError:
        raise TemplateSyntaxError('Missing path to script.')

    # Grab any remaining arguments and return the Node.
    args = contents[2:]
    return JSIncludeNode(path, args)
