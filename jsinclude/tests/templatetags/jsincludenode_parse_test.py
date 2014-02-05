from jsinclude.templatetags.jsincludenode import JSIncludeNode
from mock import Mock

class TestJSIncludeNodeParseMethod:
    def test_no_args(self, monkeypatch):
        node = JSIncludeNode('test/path')
        context = Mock()
        res = node.parseTagArguments(context)
        assert res['named'] == {}
        assert res['static'] == []

    def test_with_name_no_static(self, monkeypatch):
        context = Mock()
        context.testName = 'testData'
        context.otherName = 'otherData'
        node = JSIncludeNode('test/path', [
            'testName',
            'otherName'
        ])
        res = node.parseTagArguments(context)
        assert res['named'] == {
            'testName': 'testData',
            'otherName': 'otherData'
        }
        assert res['static'] == []

    def test_no_name_with_static(self, monkeypatch):
        context = Mock()
        node = JSIncludeNode('test/path', [
            'testData',
            'otherData'
        ])
        res = node.parseTagArguments(context)
        assert res['named'] == {}
        assert res['static'] == [
            'testData',
            'otherData'
        ]

    def test_with_name_with_static(self, monkeypatch):
        context = Mock()
        context.testName = 'testData'
        context.otherName = 'otherData'
        node = JSIncludeNode('test/path', [
            'testName',
            'otherName',
            'moreData',
            'lastData'
        ])
        res = node.parseTagArguments(context)
        assert res['named'] == {
            'testName': 'testData',
            'otherName': 'otherData'
        }
        assert res['static'] == [
            'moreData',
            'lastdata'
        ]
