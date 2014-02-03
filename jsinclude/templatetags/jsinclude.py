from jsincludenode import JSIncludeNode
from utils import strip_quotes
from django import template
register = template.Library()

@register.tag
def jsinclude(parser, token):
    """
        Syntax::
            {% jsload <path_to_script> [{arg}] %}

        Examples::
            {% jsload /widgets/receipt.js 183.92 %}
            {% jsload /widgets/nametag.js 'John Doe' %}
    """
    # Separate all tag arguments.
    contents = token.split_contents()

    # Grab path to script.
    try:
        path = strip_quotes(contents[1])
    except IndexError:
        raise template.TemplateSyntaxError('Missing path to script.')

    # Grab any other arguments and strip leading/trailing quotes.
    arguments = map(strip_quotes, contents[2:]);

    return JSIncludeNode(path, arguments)
