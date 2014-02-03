import os
from django.conf import settings

STATIC_PATH = settings.OKONOMI_STATIC_PATH

def generate_js(paths):
    """given a list of javascript media paths, read
    them from disk and return their concatenation
    """
    if type(paths) == type(''):
        # TODO decrypt
        paths = paths.split('|')

    combined = ''
    banner = '\n/* --- jsinclude --- */\n'
    for path in paths:
        # TODO use actual setting
        full_path = os.path.join(STATIC_PATH, path)
        with open(full_path, 'r') as f:
            combined += f.read() + banner # TODO slurp file
    return combined

def strip_quotes(string):
    """Strip leading and trailing quotes from a string.
    Does nothing unless starting and ending quotes are present and
    the same type (single or double).
    """
    single = string.startswith("'") and string.endswith("'")
    double = string.startswith('"') and string.endswith('"')
    if single or double:
        return string[1:-1]
    return string
