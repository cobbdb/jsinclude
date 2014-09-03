from jsinclude.templatetags.pkg.ArgumentCollection import ArgumentCollection
from jsinclude.templatetags.pkg.JSIError import JSIError
from pytest import raises

class TestArgumentCollection:
    context = {
        'testarg1': 'testval1',
        'testarg2': 'testval2',
        'testarg3': 'testval3'
    }

    def test_no_args(self):
        args = []
        result = ArgumentCollection(self.context, args)
        assert result == {}

    def test_as_variable(self):
        args = [
            'testarg1',
            'testarg2'
        ]
        result = ArgumentCollection(self.context, args)
        assert result == {
            'testarg1': "'testval1'",
            'testarg2': "'testval2'"
        }

    def test_as_string(self):
        args = [
            'testarg3',
            'test=val',
            '"long=test value"'
        ]
        result = ArgumentCollection(self.context, args)
        assert result == {
            'testarg3': "'testval3'",
            'test': "'val'",
            'long': "'test value'"
        }

    def test_with_bad_arg(self):
        args = [
            'testarg1',
            'badarg'
        ]
        with raises(JSIError):
            result = ArgumentCollection(self.context, args)
