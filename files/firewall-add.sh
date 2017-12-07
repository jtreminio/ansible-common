#!/bin/bash
#
# Add firewall rule if it does not currently exist

RULE="${1}"
RULE=${RULE/'\n'/''}
CHECK=${RULE/'-A '/'-C '}
ADD=${RULE/'-A '/'-I '}

# This will print error to STDOUT
# Ignore output!
/sbin/iptables ${CHECK}

if [ $? -ne 0 ]; then
    /sbin/iptables ${ADD}
fi
