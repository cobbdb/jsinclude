JSInclude
=========

A Django tool to keep JavaScript out of your templates.

    {% jsinclude widgets/nametag.js John Doe %}

    $ pip install -e git://github.com/cobbdb/jsinclude.git@dcobb#egg=jsinclude

Django Settings
---------------
* ``JSINCLUDE_STATIC_PATH`` set this to whatever makes sense for your django project.
* ``JSINCLUDE_HTML_TEMPLATE`` defaults to ``<script async src="%s"></script>\n``

Requirements
------------

* ${JS} sigil in HEAD or somewhere::

    {% jsrequire /formchecking.js %}

* add ``/formchecking.js`` to ``set()`` in context

... (repeat in various templates) ...

* middleware:
    * generate key from what is in the set()
    * not cached?
        * read all the js files, concat, cache
    * insert ``<script src="/js/cache_key"></script>`` for ``${JS}``

------------------------

* License: MIT
* by Cox Media Group
* Dan Cobb <dan.cobb@coxinc.com>
* Derek Anderson <derek.anderson@coxinc.com>
