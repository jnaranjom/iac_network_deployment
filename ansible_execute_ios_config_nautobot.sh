#!/bin/sh
source /home/virtual_env/bin/activate
export ANSIBLE_HOST_KEY_CHECKING=False
export ANSIBLE_CONFIG=ansible.cfg
ansible-playbook pb_get_from_nautobot.yml --skip-tags "debug"
