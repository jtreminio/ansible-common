# from https://gist.github.com/halberom/b1f6eaed16dba1b298e8#gistcomment-1679782
# ex: - {{ dirs | modify_list('(.*)','\\1.conf') }}
import re

def modify_list(values=[], pattern='', replacement='', ignorecase=False):
    ''' Perform a `re.sub` on every item in the list'''
    if ignorecase:
        flags = re.I
    else:
        flags = 0
    _re = re.compile(pattern, flags=flags)
    return [_re.sub(replacement, value) for value in values]

class FilterModule(object):
    def filters(self):
        return {'modify_list': modify_list}
