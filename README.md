JSInclude [![Build Status](https://travis-ci.org/cobbdb/jsinclude.png?branch=master)](https://travis-ci.org/cobbdb/jsinclude) [![PyPI version](https://badge.fury.io/py/jsinclude.png)](http://badge.fury.io/py/jsinclude)
=========

### A Django 1.3+ tag to keep JavaScript out of your templates.

    $ pip install jsinclude

Example of use:
> ```HTML
<!-- template.html -->
{% load jsinclude %}
{% with 31 as age %}
    {% jsinclude widgets/profile.js "name=Jane Doe" age gender=female %}
{% endwith %}
```
```JavaScript
// profile.js
console.log('My name is ' + $jsi.name);
console.log("I'm a " + $jsi.age + ' year old ' + $jsi.gender);
```

Syntax:

    {% jsinclude <path_to_script> [{arg}] %}

-----------

## $jsi
JSInclude exposes the ``$jsi`` object scoped only to the included
template.

## $jsi.&lt;name&gt;
The ``$jsi`` object contains any Django template variables preserving
original naming. Static data can be loaded into the ``$jsi`` object by
the ``name=value`` or ``"name=long value"`` tag argument conventions.

-----------

### Configuration:

    # settings.py
    JSINCLUDE_STATIC_PATH = 'required/path/to/static/files'
    JSINCLUDE_WRAP_PATH = 'optional/path/to/custom.template'
    # Built-in DEBUG will enable/disable minification.
    DEBUG = True

### Dependencies:
* [rjsmin](http://opensource.perlig.de/rjsmin/doc-1.0/index.html)

------------------------

* License: MIT
* Dan Cobb <cobbdb@gmail.com>
* Derek Anderson <dmanderson@live.com>
