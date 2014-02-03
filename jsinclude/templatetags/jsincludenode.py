from django.template import Node, loader, Context
from django.conf import settings
from rjsmin import jsmin
from utils import strip_quotes

# Set path to wrap template.
try:
    WRAP_PATH = settings.JSINCLUDE_WRAP_PATH
except AttributeError:
    WRAP_PATH = '../templates/wrap.html'

class JSIncludeNode(Node):
    def __init__(self, path, arguments=[], wrapPath=WRAP_PATH):
        self.path = strip_quotes(path)
        self.arguments = arguments
        self.wrapPath = wrapPath

    def render(self, context):
        # Load the wrap template.
        template = loader.get_template(self.wrapPath)

        # Extract values of tag arguments.
        named = {}
        unnamed = []
        for key in self.arguments:
            try:
                # Template variables.
                value = context[key]
                named[key] = value
            except KeyError:
                # Static values.
                stripped = strip_quotes(key)
                unnamed.append(stripped)

        # Create the wrap context.
        wrapContext = Context({
            'script': self.path,
            'named': named,
            'unnamed': unnamed
        })

        # Return the rendered and minified result.
        result = template.render(wrapContext)
        return 'full:\n %s \n minified: %s' % (result, jsmin(result))
