import re
from django import template

class TagNode(template.Node):
    def __init__(self, path, arguments):
        self.path = path
        self.arguments = arguments

    def render(self, context):
        try:
            context.jsload_paths.append(self.path)
        except AttributeError:
            raise template.TemplateSyntaxError('Missing JSLoad from template context.')

        msg = self.path
        for key in self.arguments:
            value = context[key]
            msg += ', %s=%s' % (key, value)
        return '~~%s~~' % msg
