JSInclude
=========

A Django 1.3+ template tag to keep JavaScript out of your templates.

    $ pip install -e git://github.com/cobbdb/jsinclude.git@dcobb#egg=jsinclude

Example of use:

    <!-- template.html -->
    {% load jsinclude %}
    {% jsinclude widgets/nametag.js 'John Doe' %}
    {% jsinclude widgets/profile.js Jane Doe female 31 %}

Syntax:

    {% jsinclude <path_to_script> [{arg}] %}

-----------

## $jsi
JSInclude exposes the ``$jsi`` object scoped only to the included
template.

## $jsi.&lt;name&gt;
The ``$jsi`` object contains any Django template variables
preserving original naming.

## $jsi.$static
The ``$jsi`` object also contains the ``$static`` array containing
any static arguments passed into the Django template tag - preserving
order.

-----------

### Configuration:

    # settings.py
    JSINCLUDE_STATIC_PATH = STATIC_COMMON_URL

### Dependencies:
* [rjsmin](http://opensource.perlig.de/rjsmin/doc-1.0/index.html)

------------------------

* License: MIT
* by Cox Media Group
* Dan Cobb <dan.cobb@coxinc.com>
* Derek Anderson <derek.anderson@coxinc.com>
