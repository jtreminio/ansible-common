def dict_append(dictA, dictB):
    print dictA

    dictC = dictA.copy()
    dictC.update(dictB)

    return dictC

class FilterModule(object):
    def filters(self):
        return {
            'dict_append': dict_append
        }
