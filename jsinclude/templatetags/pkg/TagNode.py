from django.template import Node, loader, Context
from django.conf import settings
from rjsmin import jsmin
from .utils import stripQuotes
from .ArgumentCollection import ArgumentCollection
from .JSIError import JSIError
import os

class TagNode(Node):
    def __init__(self, path, arguments=[]):
        self.path = stripQuotes(path)
        self.arguments = arguments
        try:
            self.wrapPath = settings.JSINCLUDE_WRAP_PATH
        except AttributeError:
            self.wrapPath = 'wrap.html'

    def render(self, context):
        try:
            # Create the wrap context.
            fullPath = os.path.join(settings.JSINCLUDE_STATIC_PATH, self.path)
            wrapContext = Context({
                'script': open(fullPath, 'rb').read(),
                'tagArguments': ArgumentCollection(self.arguments, context)
            }, autoescape=False)
        except JSIError as err:
            # Something went wrong, bail out and return the error.
            return err.message

        # Load the wrap template.
        template = loader.get_template(self.wrapPath)
        result = template.render(wrapContext)

        # Do not minify if in debug mode.
        if settings.TEMPLATE_DEBUG:
            return result
        return jsmin(result)
