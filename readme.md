JSInclude
=========

A Django 1.3+ template tag to keep JavaScript out of your templates.

    $ pip install -e git://github.com/cobbdb/jsinclude.git@dcobb#egg=jsinclude

Example of use:

    <!-- template.html -->
    {% load jsinclude %}
    {% jsinclude 'widgets/nametag.js' 'John Doe' %}

Configuration:

    # settings.py
    JSINCLUDE_STATIC_PATH = STATIC_COMMON_URL

Dependencies:
* [rjsmin](http://opensource.perlig.de/rjsmin/doc-1.0/index.html)

------------------------

* License: MIT
* by Cox Media Group
* Dan Cobb <dan.cobb@coxinc.com>
* Derek Anderson <derek.anderson@coxinc.com>
