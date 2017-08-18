#!/bin/bash
#
# Add firewall rule if it does not currently exist

set -o pipefail

RULE="${1}"
RULE=${RULE/'\n'/''}
CHECK=${RULE/'-A '/'-C '}
ADD=${RULE/'-A '/'-I '}

/sbin/iptables ${CHECK} | true

if [ $? -ne 0 ]; then
    /sbin/iptables ${ADD}
fi
