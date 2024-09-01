### Workflow for adding management configuration on devices

## Description

Automation solution to setup management on network devices

## Components

- Nautobot:
    - Devices loaded into SoT | Pending to find method to load devices into Nautobot (Import?)
    - Jobs: SET MGMT IP
- Ansible:
    - Render Init config

- Console:
    - Apply initial configuration

## Workflow

1. Create devices in Nautobot
2. Set devices in the proper location
3. Run job:
    - Find available port on the mgmt sw
    - Find device mgmt port
    - Connect device to mgmt sw
    - Create new IP on MGMT prefix
    - Assign IP to MGMT interface
    - Assing IP as primary IP


## Output

New devices get set in the proper location, with a dynamically allocated IP assigned and an init configuration set on the device for remote mgmt
