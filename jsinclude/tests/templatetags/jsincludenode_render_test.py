from django.template import Node, loader, Context
from pytest import raises
from jsinclude.templatetags import JSIncludeNode
from mock import Mock, patch
from django.conf import settings

class TestJSIncludeNodeRender:
    def test_render(self, monkeypatch):
        monkeypatch(settings, 'JSINCLUDE_STATIC_PATH', 'test/wrap/path', False)
        def openMock():
            stream = Mock()
            stream.read = Mock()
            stream.read.return_value = 'some test javascript'
            return stream
        monkeypatch(__builtins__, 'open', openMock)
        node = JSIncludeNode('test/path', [
            'testField',
            'Static Data'
        ])
        result = node.render({
            'testField': 123,
            'otherField': 'abc'
        })
        assert result != ''
