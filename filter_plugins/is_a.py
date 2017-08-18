import sys

def is_a(value, type):
    if type == 'dict' and value is not None:
        return isinstance(value, dict)

    if type == 'list' and value is not None:
        return isinstance(value, list)

    if type == 'str' and value is not None:
        return isstring(value)

    return False

def isstring(s):
    # if we use Python 3
    if (sys.version_info[0] >= 3):
        return isinstance(s, str)
    # we use Python 2
    return isinstance(s, basestring)

class FilterModule(object):
    ''' jinja2 filters '''

    def filters(self):
        return {
            'is_a': is_a,
        }
