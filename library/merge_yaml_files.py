#!/usr/bin/python

from ansible.module_utils.basic import *
from ansible.utils.vars import *
from ansible.parsing.dataloader import DataLoader
from ansible.parsing.yaml.dumper import AnsibleDumper
import yaml
import tempfile
import os


def merge_files(files):
    loader = DataLoader()
    files = remove_missing_files(loader, files)
    results = dict()

    for file in files:
        contents = loader.load_from_file(file)
        results = array_merge_recursive(results, contents)

    tempfd, merged_hash_file = tempfile.mkstemp(suffix='.yml')
    yaml.dump(results, open(merged_hash_file, 'w'), Dumper=AnsibleDumper, default_flow_style=False)
    if os.environ.get('SUDO_UID'):
        os.chown(merged_hash_file, int(os.environ.get('SUDO_UID')), int(os.environ.get('SUDO_GID')))

    results.update(merged_hash_file = merged_hash_file)

    return merged_hash_file


# http://www.php2python.com/wiki/function.array-merge-recursive/
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


def remove_missing_files(loader, files):
    results = list()
    for file in files:
        if loader.is_file(file):
            results.append(file)

    return results


def main():
    module = AnsibleModule(
        argument_spec = dict(
            files = dict(required=True, default=None, type='list')
        )
    )

    try:
        files = module.params.get('files')

        module.exit_json(changed=False, meta=merge_files(files))
    except Exception as e:
        module.fail_json(changed=False, msg=repr(e))

if __name__ == '__main__':
    main()
