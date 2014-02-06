from jsinclude.templatetags.jsincludenode import JSIncludeNode
from mock import Mock

class TestJSIncludeNodeParseMethod:
    def test_no_args(self):
        node = JSIncludeNode('test/path')
        context = Mock()
        res = node.parseTagArguments(context)
        assert res['tagArguments'] == {}

    def test_with_name_no_static(self):
        node = JSIncludeNode('test/path', [
            'testName',
            'otherName'
        ])
        res = node.parseTagArguments({
            'testName': 'testData',
            'otherName': 'otherData'
        })
        assert res['tagArguments'] == {
            'testName': 'testData',
            'otherName': 'otherData'
        }

    def test_no_name_with_static(self):
        node = JSIncludeNode('test/path', [
            'testName=testData',
            'someName=otherData'
        ])
        res = node.parseTagArguments({})
        assert res['tagArguments'] == {
            'testName': 'testData',
            'someName': 'otherData'
        }

    def test_with_name_with_static(self):
        node = JSIncludeNode('test/path', [
            'testName',
            'otherName',
            'someName=moreData',
            'otherName=lastData'
        ])
        res = node.parseTagArguments({
            'testName': 'testData',
            'otherName': 'otherData'
        })
        assert res['tagArguments'] == {
            'testName': 'testData',
            'otherName': 'lastData',
            'someName': 'moreData'
        }

    def test_no_equal_sign(self):
        node = JSIncludeNode('test/path', [
            'testName=testData',
            'someNaotherData'
        ])
        with rases(TempalteSyntaxError):
            res = node.parseTagArguments({})
