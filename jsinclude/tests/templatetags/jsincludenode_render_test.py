from django.template import Node, loader, Context
from pytest import raises
from jsinclude.templatetags import JSIncludeNode
from mock import Mock, patch

class TestJSIncludeNodeRender:
    def test_render(self, monkeypatch):
        