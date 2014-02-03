from django import template
register = template.Library()

@register.simple_tag(takes_context=True)
def jsinclude(context, path, argument):
    """
        Syntax::
            {% jsload <path_to_script> [{arg}] %}

        Example::
            {% jsload /widgets/receipt.js 183.92 %}
    """
    try:
        #arguments = args
        thing = 123
    except IndexError:
        raise template.TemplateSyntaxError('Missing path to script.')

    return 'path=%s, arg=%s' % (path, argument)
