def array_merge_recursive(array1, *arrays):
    for array in arrays:
        for key, value in array.items():
            if key in array1:
                if isinstance(value, dict):
                    array[key] = array_merge_recursive(array1[key], value)
                if isinstance(value, (list, tuple)):
                    array[key] += array1[key]
        array1.update(array)
    return array1

class FilterModule(object):
    ''' jinja2 filters '''

    def filters(self):
        return {
            'deep_merge': array_merge_recursive,
        }
