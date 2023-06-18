#!/usr/bin/python

# (c) 2014, Jakub Jirutka <jakub@jirutka.cz>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

DOCUMENTATION = '''
---
module: eselect
author: Jakub Jirutka
version_added: "unknown"
short_description: Module for Gentoo's eselect
description:
  - Module for Gentoo's multi-purpose configuration and management tool eselect.
options:
  mod:
    description:
      - Name of the eselect module to run.
    required: true
  action:
    description:
      - Action of the eselect module to run.
    default: set
  options:
    description:
      - An optional options for the eselect module (space separated).
    required: false
    aliases: [value, target]
'''

EXAMPLES = '''
  - eselect: mod=editor target=/usr/bin/vim

  - eselect: mod=postgresql action=reset
'''


def run_eselect(mod, *args):
    cmd = 'eselect --brief --colour=no %s' % ' '.join(args)
    rc, out, err = mod.run_command(cmd)
    if rc != 0:
        mod.fail_json(cmd=cmd, rc=rc, stdout=out, stderr=err,
                         msg='eselect failed')
    else:
        return out


def action_set(mod, emodule, target):
    current = run_eselect(mod, emodule, 'show').strip()
    if target != current:
        run_eselect(mod, emodule, 'set', target)
        return True
    else:
        return False


def main():
    mod = AnsibleModule(
        argument_spec={
            'mod':   {'required': True},
            'action':   {'default': 'set'},
            'options':  {'aliases': ['value', 'target'], 'default': ''}
        }
    )

    emodule, action, options = (mod.params[key] for key in ['mod', 'action', 'options'])
    changed = True
    msg = ''

    if action == 'set':
        changed = action_set(mod, emodule, options)
    else:
        msg = run_eselect(mod, emodule, action, options)

    mod.exit_json(changed=changed, msg=msg)

# import module snippets
from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()

