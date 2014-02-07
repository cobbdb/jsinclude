from jsinclude.templatetags.pkg.utils import escapeQuotes

class TestEscapeQuotes:
    def test_no_quotes(self):
        string = 'abc123'
        res = escapeQuotes(string)
        assert res == string

    def test_single_quotes(self):
        single = "ab'c1''23"
        res = escapeQuotes(single)
        assert res == "ab\\'c1\\'\\'23"

    def test_double_quotes(self):
        string = 'ab"c1"23""'
        res = escapeQuotes(string)
        assert res == string

    def test_mixed_quotes(self):
        actual = "'ab'c"
        actual += '1""23"'
        res = escapeQuotes(actual)
        assert res == '\\\'ab\\\'c1""23"'
