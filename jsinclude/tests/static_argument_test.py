from jsinclude.templatetags.pkg.StaticArgument import StaticArgument
from jsinclude.templatetags.pkg.JSIError import JSIError
from pytest import raises

class TestStaticArgument:
    def test_no_equal(self):
        with raises(JSIError):
            arg = StaticArgument('noequals')

    def test_quote_effects(self):
        key = '"someN\'ame=so"meLon\g Data"'
        arg = StaticArgument(key)
        assert arg["someN\\'ame"] == "'so\"meLon\g Data'"

    def test_short_value(self):
        arg = StaticArgument('short=value')
        assert arg['short'] == "'value'"

    def test_long_value(self):
        arg = StaticArgument('"some=long value"')
        assert arg['some'] == "'long value'"

    def test_number_value(self):
        arg = StaticArgument('num=123')
        assert arg['num'] == '123'

    def test_boolean_value(self):
        arg = StaticArgument('bool=true')
        assert arg['bool'] == 'true'

        arg = StaticArgument('bool=false')
        assert arg['bool'] == 'false'

    def test_python_boolean_value(self):
        arg = StaticArgument('bool=True')
        assert arg['bool'] == "'True'"

        arg = StaticArgument('bool=False')
        assert arg['bool'] == "'False'"
