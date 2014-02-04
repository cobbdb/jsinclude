from django.template import Node, loader, Context
from django.conf import settings
from rjsmin import jsmin
from utils import stripQuotes
import os

# Set path to wrap template.
try:
    WRAP_PATH = settings.JSINCLUDE_WRAP_PATH
except AttributeError:
    WRAP_PATH = '../templates/wrap.html'

class JSIncludeNode(Node):
    def __init__(self, path, arguments=[], wrapPath=WRAP_PATH):
        self.path = stripQuotes(path)
        self.arguments = arguments
        self.wrapPath = wrapPath

    def parseTagArguments(self, context):
        named = {}
        static = []
        for key in self.arguments:
            try:
                # Template variables.
                value = context[key]
                named[key] = value
            except KeyError:
                # Static values.
                stripped = stripQuotes(key)
                static.append(stripped)
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
            'named': args['named']
            'static': args['static']
        }, autoescape=False)

        # Return the rendered and minified result.
        result = template.render(wrapContext)
        return jsmin(result)
