import re
from django import template

class JSIncludeNode(template.Node):
    def __init__(self, path, arguments):
        self.path = path
        self.arguments = arguments

    def render(self, context):
        try:
            context.jsinclude_paths.append(self.path)
        except AttributeError:
            context.jsinclude_paths = [self.path]

        msg = self.path
        for key in self.arguments:
            try:
                value = context[key]
                msg += ', %s=%s' % (key, value)
            except KeyError:
                msg += ', %s' % key
        return '~~%s~~' % msg
