#!/usr/bin/python

from ansible.module_utils.basic import *
import os

def main():
    module = AnsibleModule(
        argument_spec = dict(
            dir  = dict(required=True),
            keep = dict(required=False, default=[], type='list'),
        )
    )

    try:
        dir  = module.params.get('dir')
        keep = module.params.get('keep')

        change = False

        for f in os.listdir(dir):
            file = os.path.join(dir, f)
            if (os.path.isfile(file) or os.path.islink(file)) and f not in keep:
                os.remove(file)
                change = True

        results = {}

        module.exit_json(changed=change)
    except Exception as e:
        module.fail_json(changed=False, msg=repr(e))

if __name__ == '__main__':
    main()
