from django import template
from pytest import raises
from jsinclude.templatetags import JSIncludeNode, utils
from django.conf import settings
from mock import Mock, patch
from pytest import raises

class TestJSIncludeNodeConstruction:
    def test_no_path(self, monkeypatch):
        with raises(TypeError):
            node = JSIncludeNode()

    def test_no_args_no_wrap(self, monkeypatch):
        monkeypatch(utils, 'stripQuotes', lambda: 'stripVal')
        node = JSIncludeNode('test/path')
        assert node.path == 'stripVal'
        assert node.arguments == []
        assert node.wrapPath == '../templates/wrap.html'

    def test_no_args_with_wrap(self, monkeypatch):
        monkeypatch(utils, 'stripQuotes', lambda: 'stripVal')
        monkeypatch(settings, 'JSINCLUDE_WRAP_PATH', 'test/path', False)
        node = JSIncludeNode('test/path', wrapPath='wrap/test/path')
        assert node.path == 'stripVal'
        assert node.arguments == []
        assert node.wrapPath == 'wrap/test/path'

    def test_with_args_no_wrap(self, monkeypatch):
        monkeypatch(utils, 'stripQuotes', lambda: 'stripVal')
        node = JSIncludeNode('test/path', arguments=['foo', 'bar'])
        assert node.path == 'stripVal'
        assert node.arguments == ['foo', 'bar']
        assert node.wrapPath == '../templates/wrap.html'

    def test_with_args_with_wrap(self, monkeypatch):
        monkeypatch(utils, 'stripQuotes', lambda: 'stripVal')
        monkeypatch(settings, 'JSINCLUDE_WRAP_PATH', 'test/path', False)
        node = JSIncludeNode('test/path', arguments=['foo', 'bar'])
        assert node.path == 'stripVal'
        assert node.arguments == ['foo', 'bar']
        assert node.wrapPath == 'test/path'
