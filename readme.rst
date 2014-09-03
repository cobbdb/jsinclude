JSInclude |Build Status| |Coverage Status| |PyPI version| |Download Count|
==========================================================================

A Django 1.3+ tag to keep JavaScript out of your templates.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    $ pip install jsinclude

Example of use:

::

    <!-- template.html -->
    {% load jsinclude %}
    {% with 31 as age %}
        {% jsinclude widgets/profile.js "name=Jane Doe" age gender=female %}
    {% endwith %}

::

    // profile.js
    console.log('My name is ' + $jsi.name);
    console.log("I'm a " + $jsi.age + ' year old ' + $jsi.gender);

Syntax:

::

    {% jsinclude <path_to_script> [{arg}] %}

--------------

Django-tag API
--------------

The JSInclude tag has two sections. First argument is the script
path.

::

    # Path can be a string..
    {% jsinclude literal/path/to/script.js %}
    # ..or a context variable.
    # context['mypath'] == "my/script/path.js"
    {% jsinclude mypath %}

The second argument section is where you can pass in your template
data into the JavaScript file. There are three variable format
options, and there is no limit to the number of varialbes you can
pass in.

<template variable>
^^^^^^^^^^^^^^^^^^^

Any context variable can be directly provided as a tag argument.
JSInclude will preserve the variable’s name in the JavaScript
``$jsi`` object.

::

    # context['color'] == 'red'
    {% jsinclude shape.js color %}

name=value
^^^^^^^^^^

Static values that do not contain spaces can be set as a simple
key=value pair.

::

    {% jsinclude shape.js type=square %}

“name=long value”
^^^^^^^^^^^^^^^^^

Static values that contain spaces must be wrapped in quotes. Django 1.3
does not support arbitrary arguments in template tags, so the entire
key=value pair must be wrapped in quotes.

::

    {% jsinclude shape.js "label=my red square" %}

JavaScript API
--------------

JSInclude exposes a single JavaScript object that contains all tag
arguments. This object is scoped only to the included script, so it will
not remain in scope after the script has executed and does not alter
global namespace at any time.

::

    window.myglobal = 1234; // Works as expected.
    var myotherglobal = 1234; // Scoped only to the jsincluded script.

$jsi
^^^^

JSInclude exposes the ``$jsi`` object scoped only to the included
template.

$jsi.<name>
^^^^^^^^^^^

The ``$jsi`` object contains any Django template variables preserving
original naming. Static data can be loaded into the ``$jsi`` object by
the ``name=value`` or ``"name=long value"`` tag argument conventions.

Configuration
-------------

::

    # settings.py
    JSINCLUDE_STATIC_PATH = 'required/path/to/static/files'
    JSINCLUDE_WRAP_PATH = 'optional/path/to/custom.template'
    # Built-in TEMPLATE_DEBUG will enable/disable minification.
    TEMPLATE_DEBUG = True

Dependencies
------------

-  `rjsmin`_

--------------

-  License: MIT
-  Dan Cobb cobbdb@gmail.com

.. _rjsmin: http://opensource.perlig.de/rjsmin/doc-1.0/index.html

.. |Build Status| image:: https://travis-ci.org/cobbdb/jsinclude.png?branch=master
   :target: https://travis-ci.org/cobbdb/jsinclude
.. |Coverage Status| image:: https://coveralls.io/repos/cobbdb/jsinclude/badge.png?branch=master
   :target: https://coveralls.io/r/cobbdb/jsinclude?branch=master
.. |PyPI version| image:: https://badge.fury.io/py/jsinclude.png
   :target: http://badge.fury.io/py/jsinclude
.. |Download Count| image:: https://pypip.in/d/jsinclude/badge.png
   :target: https://pypi.python.org/pypi/jsinclude
