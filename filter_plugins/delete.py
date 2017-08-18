from jinja2.utils import soft_unicode

def delete(hash, key):
    if isinstance(hash, dict):
        hash.pop(key, None)

    if isinstance(hash, list):
        hash.remove(key)

    return hash

class FilterModule(object):
    ''' jinja2 filters '''

    def filters(self):
        return {
            'delete': delete,
        }
