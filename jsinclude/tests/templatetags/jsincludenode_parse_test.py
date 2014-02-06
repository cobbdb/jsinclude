from jsinclude.templatetags.jsincludenode import JSIncludeNode
from mock import Mock

class TestJSIncludeNodeParseMethod:
    def test_no_args(self):
        node = JSIncludeNode('test/path')
        context = Mock()
        res = node.parseTagArguments(context)
        assert res['named'] == {}
        assert res['static'] == []

    def test_with_name_no_static(self):
        node = JSIncludeNode('test/path', [
            'testName',
            'otherName'
        ])
        res = node.parseTagArguments({
            'testName': 'testData',
            'otherName': 'otherData'
        })
        assert res['named'] == {
            'testName': 'testData',
            'otherName': 'otherData'
        }
        assert res['static'] == []

    def test_no_name_with_static(self):
        node = JSIncludeNode('test/path', [
            'testData',
            'otherData'
        ])
        res = node.parseTagArguments({})
        assert res['named'] == {}
        assert res['static'] == [
            'testData',
            'otherData'
        ]

    def test_with_name_with_static(self):
        node = JSIncludeNode('test/path', [
            'testName',
            'otherName',
            'moreData',
            'lastData'
        ])
        res = node.parseTagArguments({
            'testName': 'testData',
            'otherName': 'otherData'
        })
        assert res['named'] == {
            'testName': 'testData',
            'otherName': 'otherData'
        }
        assert res['static'] == [
            'moreData',
            'lastData'
        ]
