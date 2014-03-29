from jsinclude.templatetags.pkg.ArgumentValue import ArgumentValue

class TestArgumentValue:
    def test_true_number_arg(self):
        arg = ArgumentValue(1234)
        assert arg == 1234

    def test_string_number_arg(self):
        arg = ArgumentValue('1234')
        assert arg == '1234'

    def test_string_arg(self):
        arg = ArgumentValue('abc123')
        assert arg == "'abc123'"

    def test_boolean_arg(self):
        arg = ArgumentValue('true')
        assert arg == 'true'

        arg = ArgumentValue('false')
        assert arg == 'false'
