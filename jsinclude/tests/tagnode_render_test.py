from mock import Mock, patch
from jsinclude.templatetags.pkg.TagNode import TagNode
from django.conf import settings

class TestTagNodeRender:
    # First val is $jsi props, second
    # is script string.
    tpl = '<script>(function () {var $jsi = {%s};%s}());</script>'
    context = {
        'testvar1': 'testval1',
        'testvar2': 'testval2'
    }

    def test_variable_path(self):
        node = TagNode('testvar1')
        try:
            res = node.render(self.context)
            raise AssertionError('Expected test to raise IOError')
        except IOError as err:
            assert err.filename == 'static/test/path/testval1'

    def test_bad_string_path(self):
        node = TagNode('bad/path')
        try:
            res = node.render(self.context)
            raise AssertionError('Expected test to raise IOError')
        except IOError as err:
            assert err.filename == 'static/test/path/bad/path'

    def test_good_path(self):
        node = TagNode('testpath')
        with patch('__builtin__.open') as mockOpen:
            file = Mock()
            file.read.return_value = 'testscript'
            mockOpen.return_value = file
            res = node.render(self.context)
            assert res == self.tpl % (
                '',
                'testscript'
            )
