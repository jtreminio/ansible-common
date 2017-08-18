def list_append(listA, listB):
    if isinstance(listB, list):
        listA += listB
    else:
        listA.append(listB)

    return listA

class FilterModule(object):
    def filters(self):
        return {
            'list_append': list_append
        }
