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

## Django-tag API
JSInclude accepts three types of tag arguments.

#### &lt;template variable&gt;
Any context variable can be directly provided as a tag argument.
JSInclude will preserve the variable's name in the JavaScript $jsi object.

    # context['color'] == 'red'
    {% jsinclude shape.js color %}

#### name=value
Static values that do not contain spaces can be set as a simple
key=value pair.

    {% jsinclude shape.js type=square %}

#### "name=long value"
Static values that contain spaces must be wrapped in quotes. Django 1.3
does not support arbitrary arguments to template tags, so the entire
key=value pair must be wrapped in quotes.

    {% jsinclude shape.js "label=my red square" %}

## JavaScript API
JSInclude exposes a single JavaScript object that contains all
tag arguments. This object is scoped only to the included script,
so it will not remain in scope after the script has executed and
does not alter global namespace at any time. This scope containment
means that setting variable values in global scope will require
explicitly calling into the ```window``` object.

    window.myglobal = 1234; // Works as expected.
    myotherglobal = 1234; // Scoped only to the included script.

#### $jsi
JSInclude exposes the ``$jsi`` object scoped only to the included
template.

#### $jsi.&lt;name&gt;
The ``$jsi`` object contains any Django template variables preserving
original naming. Static data can be loaded into the ``$jsi`` object by
the ``name=value`` or ``"name=long value"`` tag argument conventions.

## Configuration:

    # settings.py
    JSINCLUDE_STATIC_PATH = 'required/path/to/static/files'
    JSINCLUDE_WRAP_PATH = 'optional/path/to/custom.template'
    # Built-in TEMPLATE_DEBUG will enable/disable minification.
    TEMPLATE_DEBUG = True

## Dependencies:
* [rjsmin](http://opensource.perlig.de/rjsmin/doc-1.0/index.html)

------------------------

* License: MIT
* Dan Cobb <cobbdb@gmail.com>
* Derek Anderson <dmanderson@live.com>
