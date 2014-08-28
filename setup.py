from setuptools import setup, find_packages
setup(
    name = "jsinclude",
    version = "1.2.2",
    packages = find_packages(),
    author = "Dan Cobb",
    author_email = "cobbdb@gmail.com",
    description = "A Django 1.3+ tag to keep JavaScript out of your templates.",
    license = 'MIT',
    url = "https://github.com/cobbdb/jsinclude",
    zip_safe = False,
    keywords = "javascript, loader, templatetag, django",
    install_requires = [
        'rjsmin'
    ],
    package_data = {
        'jsinclude': [
            'templates/*.html'
        ]
    },
    include_package_data = True,
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Pre-processors',
        'Topic :: Utilities',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
    ]
)
