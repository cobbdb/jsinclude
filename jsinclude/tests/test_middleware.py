from jsinclude import middleware
from helpers import FakeRequest, FakeResponse

class TestContextProcessor:
    def test_return_empty_context(self):
        request = FakeRequest() 
        result = middleware.context_processor(request)
        assert result == {}

    def test_stick_paths_into_the_context(self):
        request = FakeRequest(okonomi_paths=['path/okonomi'])
        result = middleware.context_processor(request)
        assert result == {'okonomi_paths': ['path/okonomi']}

    def test_stick_urls_into_the_context(self):
        request = FakeRequest(okonomi_urls=['/url/to/okonomi'])
        result = middleware.context_processor(request)
        assert result == {'okonomi_urls': ['/url/to/okonomi']}

    def test_stick_both_paths_and_urls(self):
        request = FakeRequest(okonomi_paths=['path/okonomi'], 
                              okonomi_urls=['/url/to/okonomi'])
        result = middleware.context_processor(request)
        assert result['okonomi_urls'] == ['/url/to/okonomi']
        assert result['okonomi_paths'] == ['path/okonomi']


class TestOkonomiMiddleware:
    def test_early_exit_urls_and_paths_are_empty(self):
        request = FakeRequest(okonomi_paths=[], okonomi_urls=[])
        response = FakeResponse(content=middleware.OKONOMI_JS_PLACEHOLDER)
        okono_middleware = middleware.Okonomi()
        result = okono_middleware.process_response(request, response)
        assert result.content == ''

    def test_early_exit_no_paths_no_urls(self):
        request = FakeRequest()
        response = FakeResponse(content=middleware.OKONOMI_JS_PLACEHOLDER)
        okono_middleware = middleware.Okonomi()
        result = okono_middleware.process_response(request, response)
        assert result.content == ''

    def test_get_valid_combined_paths_and_urls(self):
        request = FakeRequest(okonomi_paths=['path/okonomi'], 
                              okonomi_urls=['/url/to/okonomi'])
        response = FakeResponse(content=middleware.OKONOMI_JS_PLACEHOLDER)
        okono_middleware = middleware.Okonomi()
        result = okono_middleware.process_response(request, response)
        assert '<script type="text/javascript" src="/' in result.content
        assert '/url/to/okonomi' in result.content
        assert 'path/okonomi' in result.content
        

    def test_get_multiple_valid_combined_paths_and_urls(self):
        request = FakeRequest(okonomi_paths=['path/one', 'path/two'], 
                              okonomi_urls=['/url/one', '/url/two'])
        response = FakeResponse(content=middleware.OKONOMI_JS_PLACEHOLDER)
        okono_middleware = middleware.Okonomi()
        result = okono_middleware.process_response(request, response)
        assert 'path/one"></script>' in result.content
        assert 'path/two"></script>' in result.content
        assert '<script type="text/javascript" src="/url/one"></script>' in result.content
        assert '<script type="text/javascript" src="/url/two"></script>' in result.content

    def test_get_multiple_duplicated_valid_combined_paths_and_urls(self):
        request = FakeRequest(okonomi_paths=['path/one', 'path/one'], 
                              okonomi_urls=['/url/one', '/url/one'])
        response = FakeResponse(content=middleware.OKONOMI_JS_PLACEHOLDER)
        okono_middleware = middleware.Okonomi()
        result = okono_middleware.process_response(request, response)
        assert result.content.count('/url/one') == 1
        assert result.content.count('path/one') == 1

    def test_preserve_order_on_multiple_dependencies(self):
        request = FakeRequest(okonomi_paths=['path/one', 'path/two'], 
                              okonomi_urls=['/url/one', '/url/two'])
        response = FakeResponse(content=middleware.OKONOMI_JS_PLACEHOLDER)
        okono_middleware = middleware.Okonomi()
        result = okono_middleware.process_response(request, response).content.split('\n')
        assert 'path/one"></script>' in result[0]
        assert 'path/two"></script>' in result[1]
        assert '<script type="text/javascript" src="/url/one"></script>' in result[2]
        assert '<script type="text/javascript" src="/url/two"></script>' in result[3]
