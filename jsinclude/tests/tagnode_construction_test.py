from pytest import raises
from jsinclude.templatetags.pkg.TagNode import TagNode
from django.conf import settings

class TestTagNodeConstruction:
    def test_no_path(self):
        with raises(TypeError):
            node = TagNode()

    def test_no_args_no_wrap(self):
        node = TagNode('test/path')
        assert node.path == 'test/path'
        assert node.arguments == []
        assert node.wrapPath == 'wrap.html'

    def test_no_args_with_wrap(self, monkeypatch):
        monkeypatch.setattr(settings, 'JSINCLUDE_WRAP_PATH', 'test/wrap/path', False)
        node = TagNode('test/path')
        assert node.path == 'test/path'
        assert node.arguments == []
        assert node.wrapPath == 'test/wrap/path'

    def test_with_args_no_wrap(self):
        node = TagNode('test/path', arguments=['foo', 'bar'])
        assert node.path == 'test/path'
        assert node.arguments == ['foo', 'bar']
        assert node.wrapPath == 'wrap.html'

    def test_with_args_with_wrap(self, monkeypatch):
        monkeypatch.setattr(settings, 'JSINCLUDE_WRAP_PATH', 'test/wrap/path', False)
        node = TagNode('test/path', arguments=['foo', 'bar'])
        assert node.path == 'test/path'
        assert node.arguments == ['foo', 'bar']
        assert node.wrapPath == 'test/wrap/path'
