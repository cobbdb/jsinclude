from jsinclude.templatetags.pkg.StringValue import StringValue

class TestStringValue:
    def test_string_arg(self):
        arg = StringValue('abc123')
        assert arg == "'abc123'"

    def test_boolean_arg(self):
        arg = StringValue('true')
        assert arg == 'true'

        arg = StringValue('false')
        assert arg == 'false'

    def test_python_boolean_arg(self):
        arg = StringValue('True')
        assert arg == "'True'"

        arg = StringValue('False')
        assert arg == "'False'"
