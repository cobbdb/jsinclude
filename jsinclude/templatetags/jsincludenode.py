from django.template import Node, loader, Context
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
        named = {}
        static = []
        for key in self.arguments:
            try:
                # Template variables.
                value = context[key]
                value = escapeQuotes(value)
                key = escapeQuotes(key)
                named[key] = value
            except KeyError:
                # Static values.
                key = stripQuotes(key)
                key = escapeQuotes(key)
                static.append(key)
        return {
            'named': named,
            'static': static
        }

    def render(self, context):
        # Load the wrap template.
        template = loader.get_template(self.wrapPath)

        # Extract values of tag arguments.
        args = self.parseTagArguments(context)

        # Create the wrap context.
        fullPath = os.path.join(settings.JSINCLUDE_STATIC_PATH, self.path)
        wrapContext = Context({
            'script': open(fullPath, 'rb').read(),
            'named': args['named'],
            'static': args['static']
        }, autoescape=False)

        # Return the rendered and minified result.
        result = template.render(wrapContext)
        return jsmin(result)
