from jsinclude.templatetags.pkg.StaticArgument import StaticArgument
from pytest import raises
from django.template import TemplateSyntaxError

class TestStaticArgument:
    def test_no_equal(self):
        key = 'noequals'
        with raises(TemplateSyntaxError):
            arg = StaticArgument(key)

    def test_good_key(self):
        key = 'someN"ame=someD\'ata'
        arg = StaticArgument(key)
        assert arg['someN"ame'] == "someD\\'ata"

    def test_long_value(self):
        key = '"someN\'ame=so"meLon\g Data"'
        arg = StaticArgument(key)
        assert arg["someN\\'ame"] == 'so"meLon\g Data'
