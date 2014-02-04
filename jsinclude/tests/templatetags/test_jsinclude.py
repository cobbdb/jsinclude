from mock import Mock, patch
from pytest import raises
from django.template import TemplateSyntaxError
from jsinclude.templatetags import jsinclude

class TestTemplateTag:
    def test_no_path():
        parser = Mock()
        token = Mock()
        token.split_contents = Mock(return_value=[])
        with raises(TemplateSyntaxError):
            jsinclude(parser, token)

    def test_no_args():
        parser = Mock()
        token = Mock()
        token.split_contents = Mock(return_value=[
            'jsinclude',
            'test/path'
        ])
        with patch('jsinclude.JSIncludeNode') as MockNode:
            jsinclude(parser, token)
            MockNode.assert_called_with('test/path', [])

    def test_with_args():
        parser = Mock()
        token = Mock()
        token.split_contents = Mock(return_value=[
            'jsinclude',
            'test/path',
            'foo',
            'bar'
        ])
        with patch('jsinclude.JSIncludeNode') as MockNode:
            jsinclude(parser, token)
            MockNode.assert_called_with('test/path', [
                'foo',
                'bar'
            ])
