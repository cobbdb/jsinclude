from jsinclude.templatetags.pkg.StringValue import StringValue

class TestStringValue:
    def test_string_arg(self):
        arg = StringValue('abc123')
        assert arg is "'abc123'"

    def test_boolean_arg(self):
        arg = StringValue('true')
        assert arg is 'true'

        arg = StringValue('false')
        assert arg is 'false'

    def test_python_boolean_arg(self):
        arg = StringValue('True')
        assert arg is "'True'"

        arg = StringValue('False')
        assert arg is "'False'"
