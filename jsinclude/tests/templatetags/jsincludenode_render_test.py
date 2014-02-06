from django.template import Node, loader, Context
from pytest import raises
from jsinclude.templatetags.jsincludenode import JSIncludeNode
from mock import Mock, patch
from django.conf import settings

class TestJSIncludeNodeRender:
    def test_render(self, monkeypatch):
        monkeypatch.setattr(settings, 'JSINCLUDE_STATIC_PATH', 'test/wrap/path', False)
        with patch('jsinclude.templatetags.jsincludenode.open', create=True) as OpenMock:
            OpenMock.read = Mock(return_value='some test javascript')
            node = JSIncludeNode('test/path', [
                'testField',
                'Static Data',
                '"testVal"'
            ])
            result = node.render({
                'testVal': 12345
            })
            assert result != ''
