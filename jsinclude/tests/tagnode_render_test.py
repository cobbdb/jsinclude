from django.template import Node, loader, Context
from pytest import raises
from jsinclude.templatetags.pkg.TagNode import TagNode
from mock import Mock, patch
from django.conf import settings

class TestTagNodeRender:
    def test_render(self, monkeypatch):
        monkeypatch.setattr(settings, 'JSINCLUDE_STATIC_PATH', 'test/wrap/path', False)
        with patch('jsinclude.templatetags.pkg.TagNode.open', create=True) as openMock:
            with patch('jsinclude.templatetags.pkg.TagNode.jsmin', create=True) as jsminMock:
                openMock.read = Mock(return_value='some test javascript')
                node = TagNode('test/path', [
                    'someField=testField',
                    '"someData=Static Data"',
                    'testVal',
                    'someThing=testVal'
                ])
                result = node.render({
                    'testVal': '12345'
                })
                assert jsminMock.called
                assert result != ''

    def test_render_with_debug(self, monkeypatch):
        monkeypatch.setattr(settings, 'JSINCLUDE_STATIC_PATH', 'test/wrap/path', False)
        monkeypatch.setattr(settings, 'TEMPLATE_DEBUG', True, False)
        with patch('jsinclude.templatetags.pkg.TagNode.open', create=True) as openMock:
            with patch('jsinclude.templatetags.pkg.TagNode.jsmin', create=True) as jsminMock:
                openMock.read = Mock(return_value='some test javascript')
                node = TagNode('test/path', [
                    'someField=testField',
                    '"someData=Static Data"',
                    'testVal',
                    'someThing=testVal'
                ])
                result = node.render({
                    'testVal': '12345'
                })
                assert not jsminMock.called
                assert result != ''
