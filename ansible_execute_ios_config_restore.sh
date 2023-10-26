#!/bin/sh
source /home/virtual_env/bin/activate
export ANSIBLE_HOST_KEY_CHECKING=False
export ANSIBLE_CONFIG=ansible.cfg
ansible-playbook pb_ios_config_restore.yml --skip-tags "debug"
