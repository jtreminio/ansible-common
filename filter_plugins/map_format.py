# from https://gist.github.com/halberom/b1f6eaed16dba1b298e8
# ex: "{{ mylist | map('map_format', '%s.conf' ) | list }}"

# This code is essentially a direct copy of the jinja 'format' filter with
# some minor mods to the args and their use, see do_format in
# https://github.com/mitsuhiko/jinja2/blob/master/jinja2/filters.py
# for the original

from jinja2.utils import soft_unicode

def map_format(value, pattern):
    """
    Apply python string formatting on an object:
    .. sourcecode:: jinja
        {{ "%s - %s"|format("Hello?", "Foo!") }}
            -> Hello? - Foo!
    """
    return soft_unicode(pattern) % (value)

class FilterModule(object):
    ''' jinja2 filters '''

    def filters(self):
        return {
            'map_format': map_format,
        }
