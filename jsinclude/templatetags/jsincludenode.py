from django.template import Node, loader, Context, TemplateSyntaxError
from django.conf import settings
from rjsmin import jsmin
from .utils import stripQuotes, escapeQuotes
import os

class JSIncludeNode(Node):
    def __init__(self, path, arguments=[]):
        self.path = stripQuotes(path)
        self.arguments = arguments
        try:
            self.wrapPath = settings.JSINCLUDE_WRAP_PATH
        except AttributeError:
            self.wrapPath = 'wrap.html'

    def parseTagArguments(self, context):
        data = {}
        for key in self.arguments:
            try:
                # Template variables.
                value = context[key]
                value = escapeQuotes(value)
                key = escapeQuotes(key)
                data[key] = value
            except KeyError:
                # Static values are name=value format.
                try:
                    key = stripQuotes(key)
                    tokens = key.split('=', 1)
                    name = escapeQuotes(tokens[0])
                    value = escapeQuotes(tokens[1])
                    data[name] = value
                except IndexError:
                    raise TemplateSyntaxError('JSInclude: Static data must be name=value.')
        return data

    def render(self, context):
        # Load the wrap template.
        template = loader.get_template(self.wrapPath)

        # Create the wrap context.
        fullPath = os.path.join(settings.JSINCLUDE_STATIC_PATH, self.path)
        wrapContext = Context({
            'script': open(fullPath, 'rb').read(),
            'tagArguments': self.parseTagArguments(context)
        }, autoescape=False)

        # Return the rendered and minified result.
        result = template.render(wrapContext)
        return jsmin(result)
