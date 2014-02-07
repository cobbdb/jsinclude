from jsinclude.templatetags.pkg.utils import stripQuotes

class TestStripQuotes:
    def test_no_quotes(self):
        string = 'abc123'
        res = stripQuotes(string)
        assert res == string

    def test_one_quote_left(self):
        single = "'abc123"
        res = stripQuotes(single)
        assert res == single

        double = '"abc123'
        res = stripQuotes(double)
        assert res == double

    def test_one_quote_right(self):
        single = "abc123'"
        res = stripQuotes(single)
        assert res == single

        double = 'abc123"'
        res = stripQuotes(double)
        assert res == double

    def test_two_quotes(self):
        res = stripQuotes("'abc123'")
        assert res == "abc123"

        res = stripQuotes('"abc123"')
        assert res == 'abc123'
