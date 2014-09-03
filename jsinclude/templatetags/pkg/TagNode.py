from django.template import Node, loader, Context
from django.conf import settings
from rjsmin import jsmin
from .utils import stripQuotes, fin
from .ArgumentCollection import ArgumentCollection
from .PathArgument import PathArgument
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
            pathArg = PathArgument(context, self.path)
            fullPath = os.path.join(settings.JSINCLUDE_STATIC_PATH, pathArg)
            wrapContext = Context({
                'script': fin(fullPath),
                'tagArguments': ArgumentCollection(context, self.arguments)
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
