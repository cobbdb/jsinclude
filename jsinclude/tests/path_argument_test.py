from jsinclude.templatetags.pkg.PathArgument import PathArgument

class TestPathArgument:
    context = {
        'testarg1': 'testval1',
        'testarg2': 'testval2'
    }

    def test_empty_path(self):
        path = ''
        result = PathArgument(self.context, path)
        assert result == ''

    def test_as_variable(self):
        path = 'testarg2'
        result = PathArgument(self.context, path)
        assert result == 'testval2'

    def test_as_string(self):
        path = 'badarg123'
        result = PathArgument(self.context, path)
        assert result == 'badarg123'
