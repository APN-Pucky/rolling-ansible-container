#!/bin/bash
if ! command -v ansible &> /dev/null
then
    ####################
    # Install Ansible  #
    ####################
    if command -v pip3 &> /dev/null
    then
        ####################
        # Install Pip3     #
        ####################
        if command -v apt &> /dev/null
        then
            #apt update
            apt install python3-pip
        elif command -v apt-get &> /dev/null
        then
            #apt-get update
            apt-get install python3-pip
        elif command -v yum &> /dev/null
        then
            #yum update -y
            yum install -y python3-pip
        elif command -v dnf &> /dev/null
        then
            dnf install  python3-pip
        elif command -v emerge &> /dev/null
        then
            emerge -q dev-python/pip
        fi
    fi
    # We opt for a pip user install to avoid messing with the system python
    # installation. This allows us to uninstall ansible easier later on.
    python3 -m pip install --user ansible
fi
