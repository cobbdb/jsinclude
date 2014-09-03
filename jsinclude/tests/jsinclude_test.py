from mock import Mock, patch
from pytest import raises
from django.template import TemplateSyntaxError
from jsinclude.templatetags.jsinclude import jsinclude

class TestTemplateTag:
    def setup_method(self, method):
        self.parser = Mock()
        self.token = Mock()
        self.token.split_contents = Mock()

    def test_no_path(self):
        self.token.split_contents.return_value = [
            'jsinclude'
        ]
        with raises(TemplateSyntaxError):
            jsinclude(self.parser, self.token)

    @patch('jsinclude.templatetags.jsinclude.TagNode')
    def test_no_args(self, mockNode):
        self.token.split_contents.return_value = [
            'jsinclude',
            'test/path'
        ]
        jsinclude(self.parser, self.token)
        mockNode.assert_called_with('test/path', [])

    @patch('jsinclude.templatetags.jsinclude.TagNode')
    def test_with_args(self, mockNode):
        self.token.split_contents.return_value = [
            'jsinclude',
            'test/path',
            'foo',
            'bar'
        ]
        jsinclude(self.parser, self.token)
        mockNode.assert_called_with('test/path', [
            'foo',
            'bar'
        ])
