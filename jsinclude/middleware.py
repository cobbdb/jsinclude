from django.conf import settings

JS_PLACEHOLDER = '${JSREQUIRE}'
STATIC_URL = settings.OKONOMI_STATIC_URL
HTML_TEMPLATE = '<script async src="%s"></script>'

class JSInclude:
    """
    The okonomi middleware prepares unique combinations of
    javascript includes for rendered django templates. It stores
    the combined javascript in memcache for fast serving by a
    view used as a single point of javascript inclusion.
    """
    def removethis_process_request(self, request):
        request.jsinclude_paths = []

    def removethis_process_response(self, request, response):
        script = ''
        included_paths = []

        # Cannot assume that jsload_paths has been set.
        # See: <link to docs>
        try:
            all_paths = request.jsinclude_paths
        except AttributeError:
            all_paths = []

        # Add each script once, skipping subsequent duplicates.
        for path in all_paths:
            if path not in included_paths:
                included_paths.append(path)
                url = STATIC_URL + path
                script += (HTML_TEMPLATE % url)

        # Cast to string to avoid possible UnicodeDecodeErrors.
        script_str = str(script)
        response.content = response.content.replace(JS_PLACEHOLDER, script_str)
        return response

def context_processor(request):
    """ Create paths list in the template context. """
    return {
        'jsinclude_paths': []
    }
