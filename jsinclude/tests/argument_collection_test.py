from jsinclude.templatetags.pkg.ArgumentCollection import ArgumentCollection

class TestArgumentCollection:
    context = {
        
    }

    def test_no_equal(self):
        with raises(JSIError):
            arg = StaticArgument('noequals')

    def test_quote_effects(self):
        key = '"someN\'ame=so"meLon\g Data"'
        arg = StaticArgument(key)
        assert arg["someN\\'ame"] == "'so\"meLon\g Data'"
