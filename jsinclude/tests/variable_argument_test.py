from jsinclude.templatetags.pkg.VariableArgument import VariableArgument
from pytest import raises

class TestVariableArgument:
    def test_bad_key(self):
        key = 'nothere'
        context = {}
        with raises(KeyError):
            arg = VariableArgument(key, context)

    def test_string_arg(self):
        key = 'string'
        context = {
            'string': 'someData',
            'otherName': 'otherData'
        }
        arg = VariableArgument(key, context)
        assert arg[key] == "'someData'"

    def test_number_arg(self):
        key = 'num'
        context = {
            'num': 123,
            'otherName': 'otherData'
        }
        arg = VariableArgument(key, context)
        assert arg[key] == 123

    def test_boolean_arg(self):
        key = 'bool'
        context = {
            'bool': 'true',
            'otherName': 'otherData'
        }
        arg = VariableArgument(key, context)
        assert arg[key] == 'true'

        context['bool'] = 'false'
        arg = VariableArgument(key, context)
        assert arg[key] == 'false'
