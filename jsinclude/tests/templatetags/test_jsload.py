from django import template
from pytest import raises
from jsload.templatetags import okonomi as tags

class TestJSRequireNode:
    # TODO: This should not test the exact return statement.
    # Only test that a template error was thrown.
    def test_raise_when_nothing_is_passed(self):
        exc = raises(template.TemplateSyntaxError, tags.JSRequireNode)
        assert exc.value.args[0] == 'Expected either a relative path or a fully qualified url. Got nothing'

    # TODO: This should not test the exact return statement.
    # Only test that a template error was thrown.
    def test_raise_when_both_are_passed(self):
        exc = raises(template.TemplateSyntaxError, tags.JSRequireNode, path='/', url='/')
        assert exc.value.args[0] == 'Expected either a relative path or a fully qualified url. Got both'

    def test_render_correctly(self):
        js_require = tags.JSRequireNode(path='/')
        result = js_require.render([])
        assert result == '<!-- requires / -->'
