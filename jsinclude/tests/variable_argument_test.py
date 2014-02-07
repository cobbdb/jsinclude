from jsinclude.templatetags.pkg.VariableArgument import VariableArgument
from pytest import raises

class TestVariableArgument:
    def test_bad_key(self):
        key = 'nothere'
        context = {}
        with raises(KeyError):
            arg = VariableArgument(key, context)

    def test_good_key(self):
        key = 'someName'
        context = {
            'someName': 'someData',
            'otherName': 'otherData'
        }
        arg = VariableArgument(key, context)
        assert arg['someName'] == 'someData'

    def test_number_arg(self):
        key = 'someName'
        context = {
            'someName': 123,
            'otherName': 'otherData'
        }
        arg = VariableArgument(key, context)
        assert arg['someName'] == 123
