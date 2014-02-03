from django.conf.urls.defaults import patterns, url
from jsinclude.views import JSIncludeJavascript

urlpatterns = patterns('',
    url(r'^(?P<combined_path>.+)$', JSIncludeJavascript.as_view()),
)
