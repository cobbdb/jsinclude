from django.core.cache import cache
from django.http import Http404, HttpResponse
from django.views.generic.base import View
from jsinclude.utils import generate_js

class JSIncludeJavascript:
    """
    OkonomiJavascript serves combined javascript files from cache, regenerating
    them if necessary.
    """
    def get(self, *args, **kwargs):
        try:
            combined_path = kwargs['combined_path']
        except KeyError, e:
            logging.error('malformed request for javascript: %s' % e)
            raise Http404('Combined script not found.')

        cache_key = 'jsinclude:%s' % combined_path
        js = cache.get(cache_key)
        if js is None:
            js = generate_js(combined_path)

        cache.set(cache_key, js)

        return HttpResponse(js, mimetype="text/javascript")
