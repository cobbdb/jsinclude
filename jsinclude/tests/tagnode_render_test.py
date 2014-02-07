from django.template import Node, loader, Context
from pytest import raises
from jsinclude.templatetags.pkg.TagNode import TagNode
from mock import Mock, patch
from django.conf import settings

class TestTagNodeRender:
    def test_render(self, monkeypatch):
        monkeypatch.setattr(settings, 'JSINCLUDE_STATIC_PATH', 'test/wrap/path', False)
        with patch('jsinclude.templatetags.pkg.TagNode.open', create=True) as OpenMock:
            OpenMock.read = Mock(return_value='some test javascript')
            node = TagNode('test/path', [
                'someField=testField',
                '"someData=Static Data"',
                'testVal',
                'someThing=testVal'
            ])
            result = node.render({
                'testVal': '12345'
            })
            assert result != ''
